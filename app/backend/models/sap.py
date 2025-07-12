from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class SalesOrderStatus(str, Enum):
    OPEN = "Open"
    IN_PROCESS = "In Process"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    BLOCKED = "Blocked"
    PARTIALLY_DELIVERED = "Partially Delivered"
    FULLY_DELIVERED = "Fully Delivered"
    PARTIALLY_BILLED = "Partially Billed"
    FULLY_BILLED = "Fully Billed"

class SalesOrderItem(BaseModel):
    item_number: str
    material_number: str
    description: str
    quantity: float
    unit_price: float
    net_value: float
    delivery_date: Optional[str] = None
    plant: Optional[str] = None
    storage_location: Optional[str] = None
    
    # Status fields
    confirmation_status: Optional[str] = None
    delivery_status: Optional[str] = None
    billing_status: Optional[str] = None

class SalesOrderInfo(BaseModel):
    order_number: str
    order_type: str
    customer: str
    customer_name: str
    status: SalesOrderStatus
    created_date: str
    total_net_amount: float
    currency: str
    sales_organization: str
    distribution_channel: str
    division: str
    requested_delivery_date: str
    payment_terms: str
    items: List[SalesOrderItem] = []
    
    # Additional SAP fields
    sold_to_party: Optional[str] = None
    ship_to_party: Optional[str] = None
    bill_to_party: Optional[str] = None
    payer_party: Optional[str] = None
    sales_group: Optional[str] = None
    sales_office: Optional[str] = None
    reason_for_rejection: Optional[str] = None
    overall_billing_status: Optional[str] = None
    overall_delivery_status: Optional[str] = None

class SapApiResponse(BaseModel):
    d: Optional[Dict[str, Any]] = None
    value: Optional[List[Dict[str, Any]]] = None
    odata_context: Optional[str] = None
    odata_count: Optional[int] = None
    odata_next_link: Optional[str] = None
    error: Optional[Dict[str, Any]] = None

class SapError(BaseModel):
    code: str
    message: Dict[str, str]
    inner_error: Optional[Dict[str, Any]] = None

class SapValidationResult(BaseModel):
    valid: bool
    data: Optional[Any] = None
    errors: Optional[List[SapError]] = None
    warnings: Optional[List[str]] = None
    last_validated: datetime
    validation_source: str  # 'cache' | 'api' | 'mock'