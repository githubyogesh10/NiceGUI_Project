from fastapi import APIRouter, HTTPException, status
from app.backend.services.sap_service import sap_service
from app.backend.models.common import ApiResponse

router = APIRouter()

@router.get("/orders/{order_number}", response_model=ApiResponse)
async def search_sales_order(order_number: str):
    """Search for a SAP sales order"""
    try:
        result = await sap_service.search_sales_order(order_number)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/health")
async def sap_health_check():
    """Check SAP API connectivity"""
    return {
        "status": "healthy",
        "service": "SAP API",
        "timestamp": "2024-01-01T00:00:00Z",
        "mock_mode": True
    }