from typing import Dict, List

# UI Theme Constants
SKY_COLORS = {
    'primary': '#0072c6',
    'secondary': '#00a1de', 
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
    'info': '#3b82f6',
    'light': '#f8f9fa',
    'dark': '#1f2937',
    'gradient': 'linear-gradient(to right, #ff8c00 5%, #f80032 25%, #ff00a0 45%, #8c28ff 65%, #0023ff 82%, #19a0ff 96%)'
}

# Form validation messages
VALIDATION_MESSAGES = {
    'required': '{field} is required',
    'email': 'Please enter a valid email address',
    'min_length': '{field} must be at least {min} characters',
    'max_length': '{field} must not exceed {max} characters',
    'min_value': '{field} must be at least {min}',
    'max_value': '{field} must not exceed {max}',
    'positive_number': '{field} must be a positive number',
    'invalid_format': '{field} has an invalid format'
}

# Form step configuration
FORM_STEPS = [
    {
        'id': 'customer',
        'title': 'Customer Details',
        'description': 'Basic request and customer information',
        'icon': 'person'
    },
    {
        'id': 'line_items',
        'title': 'Line Items', 
        'description': 'Invoice line items and amounts',
        'icon': 'list'
    },
    {
        'id': 'regional',
        'title': 'Regional Specifics',
        'description': 'Region-specific requirements',
        'icon': 'public'
    },
    {
        'id': 'review',
        'title': 'Review & Submit',
        'description': 'Review and submit request',
        'icon': 'check_circle'
    }
]

# Navigation items
NAVIGATION_ITEMS = [
    {
        'id': 'home',
        'label': 'Home',
        'icon': 'home',
        'path': '/',
        'description': 'Dashboard and quick actions'
    },
    {
        'id': 'billing',
        'label': 'Create Billing Request',
        'icon': 'description',
        'path': '/billing',
        'description': 'Create new billing request'
    },
    {
        'id': 'search',
        'label': 'Search Sales Order',
        'icon': 'search',
        'path': '/search',
        'description': 'Search SAP sales orders'
    },
    {
        'id': 'about',
        'label': 'About',
        'icon': 'info',
        'path': '/about',
        'description': 'Application information'
    }
]

# Status badge configurations
STATUS_BADGES = {
    'DRAFT': {'class': 'sky-badge-warning', 'text': 'Draft'},
    'SUBMITTED': {'class': 'sky-badge-info', 'text': 'Submitted'},
    'UNDER_REVIEW': {'class': 'sky-badge-warning', 'text': 'Under Review'},
    'APPROVED': {'class': 'sky-badge-success', 'text': 'Approved'},
    'REJECTED': {'class': 'sky-badge-danger', 'text': 'Rejected'},
    'PROCESSING': {'class': 'sky-badge-info', 'text': 'Processing'},
    'COMPLETED': {'class': 'sky-badge-success', 'text': 'Completed'},
    'CANCELLED': {'class': 'sky-badge-danger', 'text': 'Cancelled'}
}

# Table column configurations
TABLE_COLUMNS = {
    'line_items': [
        {'key': 'description', 'title': 'Description', 'width': '200px'},
        {'key': 'sap_material_number', 'title': 'SAP Material', 'width': '120px'},
        {'key': 'wbs_code', 'title': 'WBS Code', 'width': '100px'},
        {'key': 'number_of_units', 'title': 'Units', 'width': '80px', 'align': 'center'},
        {'key': 'unit_price', 'title': 'Unit Price', 'width': '100px', 'align': 'right'},
        {'key': 'net_amount', 'title': 'Net Amount', 'width': '100px', 'align': 'right'},
        {'key': 'commission_value', 'title': 'Commission', 'width': '100px', 'align': 'right'},
        {'key': 'vat_percent', 'title': 'VAT %', 'width': '80px', 'align': 'center'},
        {'key': 'gross_amount', 'title': 'Gross Amount', 'width': '100px', 'align': 'right'},
        {'key': 'actions', 'title': 'Actions', 'width': '80px', 'align': 'center'}
    ],
    'billing_requests': [
        {'key': 'submission_id', 'title': 'Request ID', 'width': '120px'},
        {'key': 'customer_company_name', 'title': 'Customer', 'width': '200px'},
        {'key': 'type_of_request', 'title': 'Type', 'width': '100px'},
        {'key': 'total_gross_amount', 'title': 'Amount', 'width': '120px', 'align': 'right'},
        {'key': 'currency', 'title': 'Currency', 'width': '80px'},
        {'key': 'status', 'title': 'Status', 'width': '100px'},
        {'key': 'submission_date', 'title': 'Date', 'width': '100px'},
        {'key': 'actions', 'title': 'Actions', 'width': '80px', 'align': 'center'}
    ]
}

# File upload constraints
FILE_UPLOAD = {
    'max_size': 10 * 1024 * 1024,  # 10MB
    'allowed_types': ['.pdf', '.xlsx', '.xls', '.csv', '.png', '.jpg', '.jpeg'],
    'max_files': 5
}

# Pagination settings
PAGINATION = {
    'default_page_size': 25,
    'page_size_options': [10, 25, 50, 100],
    'max_page_size': 1000
}

# Date/time formats
DATE_FORMATS = {
    'display': 'DD/MM/YYYY',
    'input': 'YYYY-MM-DD',
    'api': 'YYYY-MM-DDTHH:mm:ss.sssZ',
    'filename': 'YYYYMMDD_HHmmss'
}

# Error messages for common scenarios
ERROR_MESSAGES = {
    'network_error': 'Network error occurred. Please check your connection.',
    'server_error': 'Server error occurred. Please try again later.',
    'validation_error': 'Please correct the highlighted fields.',
    'unauthorized': 'You are not authorized to perform this action.',
    'not_found': 'The requested resource was not found.',
    'timeout': 'Request timed out. Please try again.',
    'file_too_large': 'File size exceeds the maximum limit.',
    'invalid_file_type': 'Invalid file type. Please select a supported file.',
    'upload_failed': 'File upload failed. Please try again.'
}

# Success messages
SUCCESS_MESSAGES = {
    'form_submitted': 'Form submitted successfully!',
    'draft_saved': 'Draft saved successfully!',
    'file_uploaded': 'File uploaded successfully!',
    'data_exported': 'Data exported successfully!',
    'settings_saved': 'Settings saved successfully!'
}

def get_status_badge_config(status: str) -> Dict[str, str]:
    """Get badge configuration for a status"""
    return STATUS_BADGES.get(status, {'class': 'sky-badge-info', 'text': status})

def get_table_columns(table_type: str) -> List[Dict[str, str]]:
    """Get column configuration for a table type"""
    return TABLE_COLUMNS.get(table_type, [])

def format_validation_message(message_key: str, **kwargs) -> str:
    """Format validation message with parameters"""
    template = VALIDATION_MESSAGES.get(message_key, message_key)
    return template.format(**kwargs)