from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime
from enum import Enum

class LoadingState(str, Enum):
    IDLE = "idle"
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"

class SelectOption(BaseModel):
    value: str
    label: str
    disabled: bool = False
    metadata: Optional[Dict[str, Any]] = None

class ApiResponse(BaseModel):
    data: Any
    success: bool
    message: Optional[str] = None
    errors: Optional[List[str]] = None
    warnings: Optional[List[str]] = None
    timestamp: datetime
    request_id: Optional[str] = None

class ValidationError(BaseModel):
    field: str
    message: str
    code: Optional[str] = None

class User(BaseModel):
    id: str
    email: str
    name: str
    roles: List[str]
    department: Optional[str] = None
    company_code: Optional[str] = None
    permissions: Optional[List[str]] = None

class PaginationParams(BaseModel):
    page: int = 1
    limit: int = 50
    sort_by: Optional[str] = None
    sort_order: str = "asc"  # 'asc' | 'desc'

class FilterParams(BaseModel):
    search: Optional[str] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    status: Optional[str] = None
    region: Optional[str] = None