from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from app.backend.models.billing import BillingRequest, BillingSubmissionResponse
from app.backend.models.common import ApiResponse
from app.backend.services.billing_service import billing_service

router = APIRouter()

@router.post("/submit", response_model=ApiResponse)
async def submit_billing_request(request: BillingRequest):
    """Submit a new billing request"""
    try:
        result = await billing_service.create_billing_request(request)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/{request_id}", response_model=BillingRequest)
async def get_billing_request(request_id: str):
    """Get a billing request by ID"""
    request = await billing_service.get_billing_request(request_id)
    if not request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Billing request not found"
        )
    return request

@router.get("/", response_model=List[BillingRequest])
async def list_billing_requests(user_id: Optional[str] = None):
    """List all billing requests"""
    return await billing_service.list_billing_requests(user_id)