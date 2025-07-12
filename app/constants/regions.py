from typing import Dict, List, Any

# Regional configuration data
REGIONS = {
    'UK': {
        'code': 'UK',
        'name': 'UK&I',
        'full_name': 'United Kingdom & Ireland',
        'description': 'United Kingdom and Ireland billing requirements',
        'default_currency': 'GBP',
        'supported_currencies': ['GBP', 'EUR', 'USD'],
        'time_zone': 'Europe/London',
        'date_format': 'DD/MM/YYYY',
        'decimal_separator': '.',
        'thousand_separator': ','
    },
    'DACH': {
        'code': 'DACH',
        'name': 'DACH',
        'full_name': 'Deutschland, Austria, Switzerland',
        'description': 'Deutschland, Austria, and Switzerland billing requirements',
        'default_currency': 'EUR',
        'supported_currencies': ['EUR', 'CHF', 'USD', 'GBP', 'CZK'],
        'time_zone': 'Europe/Berlin',
        'date_format': 'DD.MM.YYYY',
        'decimal_separator': ',',
        'thousand_separator': '.'
    },
    'ITALY': {
        'code': 'ITALY',
        'name': 'Italy',
        'full_name': 'Italy',
        'description': 'Italian billing requirements and regulations',
        'default_currency': 'EUR',
        'supported_currencies': ['EUR', 'USD', 'GBP'],
        'time_zone': 'Europe/Rome',
        'date_format': 'DD/MM/YYYY',
        'decimal_separator': ',',
        'thousand_separator': '.'
    }
}

# Regional validation rules
REGIONAL_VALIDATION_RULES = {
    'UK': {
        'required_fields': ['uk_type_of_request', 'uk_company', 'uk_manual_billing_reason'],
        'vat_validation': {
            'required': False,
            'pattern': r'^GB\d{9}$|^GB\d{12}$'
        },
        'postal_code_pattern': r'^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$'
    },
    'DACH': {
        'required_fields': ['dach_type_of_request', 'dach_currency', 'dach_payment_terms', 'dach_company'],
        'vat_validation': {
            'required': True,
            'patterns': {
                'DE': r'^DE\d{9}$',
                'AT': r'^ATU\d{8}$',
                'CH': r'^CHE-\d{3}\.\d{3}\.\d{3}$'
            }
        }
    },
    'ITALY': {
        'required_fields': ['italy_type_of_request', 'italy_company'],
        'vat_validation': {
            'required': True,
            'pattern': r'^IT\d{11}$'
        },
        'fiscal_code_pattern': r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$'
    }
}

def get_region_config(region_code: str) -> Dict[str, Any]:
    """Get configuration for a specific region"""
    return REGIONS.get(region_code, {})

def get_supported_regions() -> List[Dict[str, str]]:
    """Get list of supported regions"""
    return [
        {
            'code': region['code'],
            'name': region['name'],
            'description': region['description']
        }
        for region in REGIONS.values()
    ]

def get_region_currencies(region_code: str) -> List[str]:
    """Get supported currencies for a region"""
    region = REGIONS.get(region_code, {})
    return region.get('supported_currencies', [])

def get_region_validation_rules(region_code: str) -> Dict[str, Any]:
    """Get validation rules for a specific region"""
    return REGIONAL_VALIDATION_RULES.get(region_code, {})