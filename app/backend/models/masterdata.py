from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.backend.models.common import SelectOption

class CompanyData(BaseModel):
    code: str
    name: str
    region: str
    currency: str
    active: bool = True

class RegionConfig(BaseModel):
    code: str
    name: str
    description: str
    companies: List[CompanyData]
    currencies: List[str]
    specific_fields: Dict[str, Any]

class DropdownOptions(BaseModel):
    company_codes: List[SelectOption]
    request_types: List[SelectOption]
    currencies: List[SelectOption]
    departments: List[SelectOption]
    regions: List[SelectOption]
    
    # UK specific
    uk_companies: List[SelectOption]
    uk_request_types: List[SelectOption]
    uk_billing_reasons: List[SelectOption]
    
    # DACH specific
    dach_companies: List[SelectOption]
    dach_request_types: List[SelectOption]
    dach_currencies: List[SelectOption]
    dach_payment_terms: List[SelectOption]
    
    # Italy specific
    italy_companies: List[SelectOption]
    italy_request_types: List[SelectOption]

class MasterDataResponse(BaseModel):
    regions: List[RegionConfig]
    dropdown_options: DropdownOptions
    last_updated: str
    version: str