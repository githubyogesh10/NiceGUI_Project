from typing import List, Dict, Any
from app.backend.models.billing import BillingRequest
from app.backend.models.common import ValidationError

class ValidationService:
    
    async def validate_billing_request(self, request: BillingRequest) -> Dict[str, Any]:
        """Validate a complete billing request"""
        errors = []
        warnings = []
        
        # Basic field validation
        errors.extend(self._validate_basic_fields(request))
        
        # Customer validation
        errors.extend(self._validate_customer_details(request))
        
        # Line items validation
        errors.extend(self._validate_line_items(request))
        
        # Regional validation
        errors.extend(self._validate_regional_data(request))
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def _validate_basic_fields(self, request: BillingRequest) -> List[str]:
        """Validate basic required fields"""
        errors = []
        
        if not request.requested_by:
            errors.append("Requested by is required")
        
        if not request.company_code:
            errors.append("Company code is required")
        
        if not request.type_of_request:
            errors.append("Type of request is required")
        
        if not request.department:
            errors.append("Department is required")
        
        if not request.currency:
            errors.append("Currency is required")
        
        return errors
    
    def _validate_customer_details(self, request: BillingRequest) -> List[str]:
        """Validate customer information"""
        errors = []
        
        if not request.customer_company_name:
            errors.append("Customer company name is required")
        
        if not request.address:
            errors.append("Customer address is required")
        
        if not request.country:
            errors.append("Customer country is required")
        
        if request.client_email and not self._is_valid_email(request.client_email):
            errors.append("Invalid email address format")
        
        return errors
    
    def _validate_line_items(self, request: BillingRequest) -> List[str]:
        """Validate line items"""
        errors = []
        
        if not request.line_items:
            errors.append("At least one line item is required")
            return errors
        
        for i, item in enumerate(request.line_items):
            if not item.description:
                errors.append(f"Line item {i + 1}: Description is required")
            
            if item.number_of_units <= 0:
                errors.append(f"Line item {i + 1}: Number of units must be greater than 0")
            
            if item.unit_price <= 0:
                errors.append(f"Line item {i + 1}: Unit price must be greater than 0")
        
        return errors
    
    def _validate_regional_data(self, request: BillingRequest) -> List[str]:
        """Validate region-specific data"""
        errors = []
        
        if not request.region:
            errors.append("Region is required")
            return errors
        
        if request.region == "UK":
            if not request.regional_data.uk:
                errors.append("UK regional data is required")
            elif request.regional_data.uk:
                uk_data = request.regional_data.uk
                if not uk_data.type_of_request:
                    errors.append("UK type of request is required")
                if not uk_data.company:
                    errors.append("UK company is required")
                if not uk_data.manual_billing_reason:
                    errors.append("UK manual billing reason is required")
        
        elif request.region == "DACH":
            if not request.regional_data.dach:
                errors.append("DACH regional data is required")
            elif request.regional_data.dach:
                dach_data = request.regional_data.dach
                if not dach_data.type_of_request:
                    errors.append("DACH type of request is required")
                if not dach_data.currency:
                    errors.append("DACH currency is required")
                if not dach_data.payment_terms:
                    errors.append("DACH payment terms are required")
                if not dach_data.company:
                    errors.append("DACH company is required")
        
        elif request.region == "ITALY":
            if not request.regional_data.italy:
                errors.append("Italy regional data is required")
            elif request.regional_data.italy:
                italy_data = request.regional_data.italy
                if not italy_data.type_of_request:
                    errors.append("Italy type of request is required")
                if not italy_data.company:
                    errors.append("Italy company is required")
        
        return errors
    
    def _is_valid_email(self, email: str) -> bool:
        """Basic email validation"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

# Global service instance
validation_service = ValidationService()