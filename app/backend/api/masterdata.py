from fastapi import APIRouter, HTTPException, status
from app.backend.services.masterdata_service import masterdata_service
from app.backend.models.masterdata import DropdownOptions

router = APIRouter()

@router.get("/dropdown-options", response_model=DropdownOptions)
async def get_dropdown_options():
    """Get all dropdown options for forms"""
    try:
        return masterdata_service.get_dropdown_options()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/regions")
async def get_regions():
    """Get available regions"""
    return [
        {"code": "UK", "name": "UK&I", "description": "United Kingdom and Ireland"},
        {"code": "DACH", "name": "DACH", "description": "Deutschland, Austria, Switzerland"},
        {"code": "ITALY", "name": "Italy", "description": "Italian market"}
    ]

@router.get("/companies/{region}")
async def get_companies_by_region(region: str):
    """Get companies for a specific region"""
    options = masterdata_service.get_dropdown_options()
    
    if region.upper() == "UK":
        return options.uk_companies
    elif region.upper() == "DACH":
        return options.dach_companies
    elif region.upper() == "ITALY":
        return options.italy_companies
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Region not found"
        )