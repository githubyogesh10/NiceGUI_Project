import re
from typing import Dict, Any, List
from app.backend.models.billing import BillingRequest

class ValidationResult:
    def __init__(self):
        self.valid = True
        self.errors = []
        self.warnings = []

async def validate_billing_request(request: BillingRequest) -> ValidationResult:
    """Validate a complete billing request"""
    result = ValidationResult()
    
    # Basic field validation
    if not request.requested_by:
        result.errors.append("Requested by is required")
        result.valid = False
    
    if not request.company_code:
        result.errors.append("Company code is required")
        result.valid = False
    
    if not request.type_of_request:
        result.errors.append("Type of request is required")
        result.valid = False
    
    if not request.department:
        result.errors.append("Department is required")
        result.valid = False
    
    if not request.currency:
        result.errors.append("Currency is required")
        result.valid = False
    
    # Customer validation
    if not request.customer_company_name:
        result.errors.append("Customer company name is required")
        result.valid = False
    
    if not request.address:
        result.errors.append("Customer address is required")
        result.valid = False
    
    if not request.country:
        result.errors.append("Customer country is required")
        result.valid = False
    
    # Email validation
    if request.client_email and not is_valid_email(request.client_email):
        result.errors.append("Invalid email address format")
        result.valid = False
    
    # Line items validation
    if not request.line_items:
        result.errors.append("At least one line item is required")
        result.valid = False
    else:
        for i, item in enumerate(request.line_items):
            if not item.description:
                result.errors.append(f"Line item {i + 1}: Description is required")
                result.valid = False
            
            if item.number_of_units <= 0:
                result.errors.append(f"Line item {i + 1}: Number of units must be greater than 0")
                result.valid = False
            
            if item.unit_price <= 0:
                result.errors.append(f"Line item {i + 1}: Unit price must be greater than 0")
                result.valid = False
    
    # Regional validation
    if not request.region:
        result.errors.append("Region is required")
        result.valid = False
    elif request.region == "UK":
        if not request.regional_data.uk:
            result.errors.append("UK regional data is required")
            result.valid = False
        elif request.regional_data.uk:
            uk_data = request.regional_data.uk
            if not uk_data.type_of_request:
                result.errors.append("UK type of request is required")
                result.valid = False
            if not uk_data.company:
                result.errors.append("UK company is required")
                result.valid = False
            if not uk_data.manual_billing_reason:
                result.errors.append("UK manual billing reason is required")
                result.valid = False
    
    return result

def is_valid_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> List[str]:
    """Validate required fields in data dictionary"""
    errors = []
    for field in required_fields:
        if not data.get(field):
            field_name = field.replace('_', ' ').title()
            errors.append(f'{field_name} is required')
    return errors

def validate_line_items(line_items: List[Dict[str, Any]]) -> List[str]:
    """Validate line items data"""
    errors = []
    
    if not line_items:
        errors.append("At least one line item is required")
        return errors
    
    for i, item in enumerate(line_items):
        if not item.get('description'):
            errors.append(f"Line item {i + 1}: Description is required")
        
        if not item.get('number_of_units') or float(item.get('number_of_units', 0)) <= 0:
            errors.append(f"Line item {i + 1}: Number of units must be greater than 0")
        
        if not item.get('unit_price') or float(item.get('unit_price', 0)) <= 0:
            errors.append(f"Line item {i + 1}: Unit price must be greater than 0")
    
    return errors