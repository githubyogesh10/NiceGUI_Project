from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RequestType(str, Enum):
    INVOICE = "INVOICE"
    CREDIT_NOTE = "CREDIT_NOTE"

class Currency(str, Enum):
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    CHF = "CHF"
    CZK = "CZK"

class Region(str, Enum):
    UK = "UK"
    DACH = "DACH"
    ITALY = "ITALY"

class BillingRequestStatus(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class LineItem(BaseModel):
    id: str
    description: str
    sap_material_number: Optional[str] = None
    wbs_code: Optional[str] = None
    number_of_units: float = Field(gt=0)
    unit_price: float = Field(gt=0)
    net_amount: float = 0.0
    commission_value: Optional[float] = 0.0
    vat_percent: Optional[float] = 0.0
    gross_amount: float = 0.0
    
    def calculate_amounts(self):
        """Calculate net and gross amounts"""
        self.net_amount = self.number_of_units * self.unit_price
        vat_amount = self.net_amount * (self.vat_percent or 0) / 100
        self.gross_amount = self.net_amount - (self.commission_value or 0) + vat_amount

class UKSpecificData(BaseModel):
    type_of_request: str
    company: str
    manual_billing_reason: str
    additional_notes: Optional[str] = None

class DACHSpecificData(BaseModel):
    type_of_request: str
    currency: str
    payment_terms: str
    company: str
    tax_code: Optional[str] = None
    customs_info: Optional[str] = None

class ItalySpecificData(BaseModel):
    type_of_request: str
    company: str
    fiscal_code: Optional[str] = None
    pec_email: Optional[str] = None
    sdi_code: Optional[str] = None

class RegionalData(BaseModel):
    uk: Optional[UKSpecificData] = None
    dach: Optional[DACHSpecificData] = None
    italy: Optional[ItalySpecificData] = None

class BillingRequest(BaseModel):
    # System fields
    id: Optional[str] = None
    submission_id: Optional[str] = None
    status: BillingRequestStatus = BillingRequestStatus.DRAFT
    submission_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None
    
    # Request details
    requested_by: str
    company_code: str
    type_of_request: RequestType
    department: str
    po_number: Optional[str] = None
    currency: Currency
    
    # Customer details
    customer_company_name: str
    sap_customer_number: Optional[str] = None
    address: str
    post_code: Optional[str] = None
    country: str
    company_reg_no: Optional[str] = None
    vat_number: Optional[str] = None
    contact_name: Optional[str] = None
    client_email: Optional[EmailStr] = None
    
    # Additional info
    payment_terms: Optional[str] = None
    invoice_header_text: Optional[str] = None
    sales_distribution_channel: Optional[str] = None
    
    # Line items
    line_items: List[LineItem] = []
    
    # Regional data
    region: Region
    regional_data: RegionalData
    
    # Calculated fields
    total_net_amount: Optional[float] = 0.0
    total_gross_amount: Optional[float] = 0.0
    total_commission: Optional[float] = 0.0
    
    def calculate_totals(self):
        """Calculate total amounts from line items"""
        self.total_net_amount = sum(item.net_amount for item in self.line_items)
        self.total_gross_amount = sum(item.gross_amount for item in self.line_items)
        self.total_commission = sum(item.commission_value or 0 for item in self.line_items)

class BillingSubmissionResponse(BaseModel):
    submission_id: str
    status: BillingRequestStatus
    message: str
    processed_at: datetime
    estimated_completion_time: Optional[datetime] = None
    tracking_url: Optional[str] = None