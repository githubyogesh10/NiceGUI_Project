from typing import Dict, Any, Optional

# SAP API configuration
SAP_API_CONFIG = {
    'base_url': 'https://sandbox.api.sap.com/s4hanacloud/sap/opu/odata/sap',
    'api_key': '7NIOHGBmJSnemCSSAKsf9FgBWGAUCwxO',
    'timeout': 30,
    'retries': 3,
    'retry_delay': 1,
    'services': {
        'sales_order': 'API_SALES_ORDER_SRV',
        'material': 'API_MATERIAL_SRV',
        'customer': 'API_BUSINESS_PARTNER',
        'product': 'API_PRODUCT_SRV'
    },
    'endpoints': {
        'sales_order': '/A_SalesOrder',
        'sales_order_item': '/A_SalesOrderItem',
        'customer': '/A_Customer',
        'material': '/A_Product'
    }
}

# SAP field mappings
SAP_FIELD_MAPPINGS = {
    'sales_order': {
        'SalesOrder': 'order_number',
        'SalesOrderType': 'order_type',
        'SoldToParty': 'customer',
        'SoldToPartyName': 'customer_name',
        'OverallSDProcessStatus': 'status',
        'CreationDate': 'created_date',
        'TotalNetAmount': 'total_net_amount',
        'TransactionCurrency': 'currency',
        'SalesOrganization': 'sales_organization',
        'DistributionChannel': 'distribution_channel',
        'Division': 'division',
        'RequestedDeliveryDate': 'requested_delivery_date',
        'CustomerPaymentTerms': 'payment_terms',
        'ShipToParty': 'ship_to_party',
        'BillToParty': 'bill_to_party',
        'PayerParty': 'payer_party',
        'SalesGroup': 'sales_group',
        'SalesOffice': 'sales_office',
        'ReasonForRejection': 'reason_for_rejection',
        'OverallBillingStatus': 'overall_billing_status',
        'OverallDeliveryStatus': 'overall_delivery_status'
    },
    'customer': {
        'Customer': 'customer_number',
        'CustomerName': 'customer_name',
        'Country': 'country',
        'Region': 'region',
        'CityName': 'city',
        'PostalCode': 'postal_code',
        'StreetName': 'address',
        'CustomerPaymentTerms': 'payment_terms',
        'CreditLimitAmount': 'credit_limit',
        'Currency': 'currency'
    }
}

# SAP error codes and messages
SAP_ERROR_CODES = {
    '404': 'Resource not found',
    '401': 'Unauthorized - Invalid API key',
    '403': 'Forbidden - Access denied',
    '429': 'Too many requests - Rate limit exceeded',
    '500': 'Internal server error',
    '503': 'Service unavailable',
    'TIMEOUT': 'Request timeout',
    'CONNECTION_ERROR': 'Connection error'
}

# Mock data for development/demo
MOCK_SAP_DATA = {
    'sales_orders': {
        '4500000001': {
            'SalesOrder': '4500000001',
            'SalesOrderType': 'Standard Order',
            'SoldToParty': '1000001',
            'SoldToPartyName': 'ABC Company Ltd',
            'OverallSDProcessStatus': 'Completed',
            'CreationDate': '2024-01-15',
            'TotalNetAmount': 15000.00,
            'TransactionCurrency': 'GBP',
            'SalesOrganization': '1000',
            'DistributionChannel': '10',
            'Division': '00',
            'RequestedDeliveryDate': '2024-02-15',
            'CustomerPaymentTerms': 'Net 30',
            'OverallBillingStatus': 'Fully Billed',
            'OverallDeliveryStatus': 'Fully Delivered'
        },
        '4500000002': {
            'SalesOrder': '4500000002',
            'SalesOrderType': 'Rush Order',
            'SoldToParty': '1000002',
            'SoldToPartyName': 'XYZ Corporation',
            'OverallSDProcessStatus': 'In Process',
            'CreationDate': '2024-02-01',
            'TotalNetAmount': 25000.00,
            'TransactionCurrency': 'EUR',
            'SalesOrganization': '1000',
            'DistributionChannel': '10',
            'Division': '00',
            'RequestedDeliveryDate': '2024-02-28',
            'CustomerPaymentTerms': 'Net 14',
            'OverallBillingStatus': 'Partially Billed',
            'OverallDeliveryStatus': 'Partially Delivered'
        }
    }
}

def get_sap_config() -> Dict[str, Any]:
    """Get SAP API configuration"""
    return SAP_API_CONFIG

def get_field_mapping(entity_type: str) -> Dict[str, str]:
    """Get field mapping for SAP entity type"""
    return SAP_FIELD_MAPPINGS.get(entity_type, {})

def get_mock_data(data_type: str, key: Optional[str] = None) -> Any:
    """Get mock SAP data for development"""
    data = MOCK_SAP_DATA.get(data_type, {})
    if key:
        return data.get(key)
    return data