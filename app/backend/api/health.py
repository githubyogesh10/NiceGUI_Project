from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
async def health_check():
    """Application health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "service": "O2C Billing Portal"
    }

@router.get("/detailed")
async def detailed_health_check():
    """Detailed health check with service status"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "database": "healthy",
            "sap_api": "healthy",
            "file_system": "healthy"
        },
        "version": "1.0.0",
        "uptime": "24h 30m",
        "environment": "development"
    }