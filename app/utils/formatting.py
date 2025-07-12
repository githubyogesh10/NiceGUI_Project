from typing import Any, Dict
import locale
from datetime import datetime

def format_currency(amount: float, currency: str = 'GBP') -> str:
    """Format currency amount with proper symbol and formatting"""
    currency_symbols = {
        'GBP': '£',
        'EUR': '€', 
        'USD': '$',
        'CHF': 'CHF',
        'CZK': 'CZK'
    }
    
    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"

def format_date(date_obj: datetime, format_type: str = 'short') -> str:
    """Format date object to string"""
    if format_type == 'short':
        return date_obj.strftime('%Y-%m-%d')
    elif format_type == 'long':
        return date_obj.strftime('%B %d, %Y')
    elif format_type == 'datetime':
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return date_obj.isoformat()

def format_number(number: float, decimal_places: int = 2) -> str:
    """Format number with proper decimal places and thousand separators"""
    return f"{number:,.{decimal_places}f}"

def format_percentage(value: float, decimal_places: int = 1) -> str:
    """Format percentage value"""
    return f"{value:.{decimal_places}f}%"

def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case"""
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_camel(name: str) -> str:
    """Convert snake_case to camelCase"""
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def format_field_name(field_name: str) -> str:
    """Format field name for display (snake_case to Title Case)"""
    return field_name.replace('_', ' ').title()

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations"""
    import re
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing periods and spaces
    filename = filename.strip('. ')
    return filename

def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"

def format_duration(seconds: int) -> str:
    """Format duration in seconds to human readable format"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}m {secs}s" if secs > 0 else f"{minutes}m"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m" if minutes > 0 else f"{hours}h"