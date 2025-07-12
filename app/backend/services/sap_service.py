import httpx
import asyncio
from typing import Optional, Dict, Any
from datetime import datetime

from app.backend.models.sap import SalesOrderInfo, SapApiResponse, SapValidationResult
from app.backend.models.common import ApiResponse
from app.config import settings

class SapService:
    def __init__(self):
        self.base_url = settings.sap_api_base_url
        self.api_key = settings.sap_api_key
        self.timeout = settings.sap_timeout
        self.retries = settings.sap_retries
    
    async def search_sales_order(self, order_number: str) -> ApiResponse:
        """Search for a sales order by number"""
        try:
            if settings.enable_mock_data:
                # Return mock data for demo purposes
                mock_data = self._get_mock_order_data(order_number)
                return ApiResponse(
                    data=mock_data,
                    success=True,
                    message="Order found (mock data)",
                    timestamp=datetime.now()
                )
            
            # Real SAP API call
            url = f"{self.base_url}/API_SALES_ORDER_SRV/A_SalesOrder('{order_number}')"
            headers = {
                "APIKey": self.api_key,
                "DataServiceVersion": "2.0",
                "Accept": "application/json"
            }
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    order_info = self._parse_sap_response(data)
                    
                    return ApiResponse(
                        data=order_info,
                        success=True,
                        message="Order found",
                        timestamp=datetime.now()
                    )
                elif response.status_code == 404:
                    return ApiResponse(
                        data=None,
                        success=False,
                        errors=["Sales order not found"],
                        timestamp=datetime.now()
                    )
                else:
                    return ApiResponse(
                        data=None,
                        success=False,
                        errors=[f"SAP API error: {response.status_code}"],
                        timestamp=datetime.now()
                    )
                    
        except httpx.TimeoutException:
            return ApiResponse(
                data=None,
                success=False,
                errors=["SAP API timeout"],
                timestamp=datetime.now()
            )
        except Exception as e:
            return ApiResponse(
                data=None,
                success=False,
                errors=[f"Error: {str(e)}"],
                timestamp=datetime.now()
            )
    
    def _get_mock_order_data(self, order_number: str) -> SalesOrderInfo:
        """Generate mock order data for testing"""
        return SalesOrderInfo(
            order_number=order_number,
            order_type="Standard Order",
            customer="1000001",
            customer_name="ABC Company Ltd",
            status=SalesOrderInfo.__annotations__['status'].__args__[0].COMPLETED,
            created_date="2024-01-15",
            total_net_amount=15000.00,
            currency="GBP",
            sales_organization="1000",
            distribution_channel="10",
            division="00",
            requested_delivery_date="2024-02-15",
            payment_terms="Net 30",
            sold_to_party="1000001",
            ship_to_party="1000001",
            bill_to_party="1000001",
            overall_billing_status="Fully Billed",
            overall_delivery_status="Fully Delivered"
        )
    
    def _parse_sap_response(self, sap_data: Dict[str, Any]) -> SalesOrderInfo:
        """Parse SAP API response into our model"""
        data = sap_data.get('d', sap_data)
        
        return SalesOrderInfo(
            order_number=data.get('SalesOrder', ''),
            order_type=data.get('SalesOrderType', ''),
            customer=data.get('SoldToParty', ''),
            customer_name=data.get('SoldToPartyName', ''),
            status=data.get('OverallSDProcessStatus', 'Unknown'),
            created_date=data.get('CreationDate', ''),
            total_net_amount=float(data.get('TotalNetAmount', 0)),
            currency=data.get('TransactionCurrency', 'EUR'),
            sales_organization=data.get('SalesOrganization', ''),
            distribution_channel=data.get('DistributionChannel', ''),
            division=data.get('Division', ''),
            requested_delivery_date=data.get('RequestedDeliveryDate', ''),
            payment_terms=data.get('CustomerPaymentTerms', ''),
            sold_to_party=data.get('SoldToParty', ''),
            ship_to_party=data.get('ShipToParty', ''),
            bill_to_party=data.get('BillToParty', ''),
            overall_billing_status=data.get('OverallBillingStatus', ''),
            overall_delivery_status=data.get('OverallDeliveryStatus', '')
        )

# Global service instance
sap_service = SapService()