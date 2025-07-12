from typing import List, Optional
from datetime import datetime
import uuid

from app.backend.models.billing import BillingRequest, BillingSubmissionResponse, BillingRequestStatus
from app.backend.models.common import ApiResponse
from app.utils.validation import validate_billing_request

class BillingService:
    def __init__(self):
        # In a real application, this would be a database
        self._requests: List[BillingRequest] = []
    
    async def create_billing_request(self, request_data: BillingRequest) -> ApiResponse:
        """Create a new billing request"""
        try:
            # Validate the request
            validation_result = await validate_billing_request(request_data)
            if not validation_result.valid:
                return ApiResponse(
                    data=None,
                    success=False,
                    errors=validation_result.errors,
                    timestamp=datetime.now()
                )
            
            # Generate IDs and set metadata
            request_data.id = str(uuid.uuid4())
            request_data.submission_id = f"BR-{datetime.now().strftime('%Y%m%d')}-{len(self._requests) + 1:04d}"
            request_data.submission_date = datetime.now()
            request_data.last_modified = datetime.now()
            request_data.status = BillingRequestStatus.SUBMITTED
            
            # Calculate totals
            for item in request_data.line_items:
                item.calculate_amounts()
            request_data.calculate_totals()
            
            # Store the request
            self._requests.append(request_data)
            
            return ApiResponse(
                data=BillingSubmissionResponse(
                    submission_id=request_data.submission_id,
                    status=request_data.status,
                    message="Billing request submitted successfully",
                    processed_at=datetime.now()
                ),
                success=True,
                message="Request submitted successfully",
                timestamp=datetime.now()
            )
            
        except Exception as e:
            return ApiResponse(
                data=None,
                success=False,
                errors=[str(e)],
                timestamp=datetime.now()
            )
    
    async def get_billing_request(self, request_id: str) -> Optional[BillingRequest]:
        """Get a billing request by ID"""
        for request in self._requests:
            if request.id == request_id:
                return request
        return None
    
    async def list_billing_requests(self, user_id: Optional[str] = None) -> List[BillingRequest]:
        """List all billing requests, optionally filtered by user"""
        if user_id:
            return [req for req in self._requests if req.requested_by == user_id]
        return self._requests
    

# Global service instance
billing_service = BillingService()