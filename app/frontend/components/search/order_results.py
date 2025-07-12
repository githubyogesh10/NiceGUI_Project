from nicegui import ui
from typing import Dict, Any, Optional

def create_order_results(order_data: Optional[Dict[str, Any]], error_message: Optional[str] = None):
    """Create order search results display"""
    
    def format_currency(amount: float, currency: str) -> str:
        """Format currency amount"""
        currency_symbols = {'GBP': '£', 'EUR': '€', 'USD': '$', 'CHF': 'CHF', 'CZK': 'CZK'}
        symbol = currency_symbols.get(currency, currency)
        return f"{symbol}{amount:,.2f}"
    
    def get_status_badge_class(status: str) -> str:
        """Get CSS class for status badge"""
        status_lower = status.lower()
        if 'completed' in status_lower or 'fully' in status_lower:
            return 'sky-badge-success'
        elif 'process' in status_lower or 'partially' in status_lower:
            return 'sky-badge-warning'
        else:
            return 'sky-badge-info'
    
    def copy_to_clipboard():
        """Copy order details to clipboard"""
        if order_data:
            import json
            details = json.dumps(order_data, indent=2)
            # Note: In a real implementation, you'd use JavaScript to copy to clipboard
            ui.notify('Order details copied to clipboard!', type='positive')
    
    def create_billing_request():
        """Navigate to create billing request with pre-filled data"""
        ui.notify('Feature coming soon: Create billing request from this order', type='info')
    
    if not order_data and not error_message:
        return
    
    # Results container
    with ui.element('div').classes('bg-gradient-to-r from-blue-50 to-blue-100 border border-blue-200 rounded-lg p-6 mt-6'):
        
        # Error message
        if error_message:
            with ui.element('div').classes('bg-yellow-100 border border-yellow-300 rounded-lg p-3 mb-4'):
                with ui.row().classes('items-center gap-2'):
                    ui.icon('warning').classes('text-yellow-600')
                    ui.label(error_message).classes('text-sm text-yellow-800')
        
        if order_data:
            # Header with status
            with ui.row().classes('w-full items-center justify-between mb-6'):
                ui.label('Order Details').classes('text-xl font-semibold text-blue-800')
                
                status = order_data.get('status', 'Unknown')
                badge_class = get_status_badge_class(status)
                with ui.element('span').classes(f'sky-badge {badge_class}'):
                    ui.label(status)
            
            # Order information grid
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6'):
                
                # Order details
                order_fields = [
                    ('Order Number', 'order_number'),
                    ('Order Type', 'order_type'),
                    ('Customer', 'customer'),
                    ('Created Date', 'created_date'),
                    ('Total Amount', None),  # Special handling
                    ('Payment Terms', 'payment_terms'),
                    ('Sales Org', 'sales_organization'),
                    ('Distribution Channel', 'distribution_channel'),
                    ('Delivery Date', 'requested_delivery_date')
                ]
                
                for label, key in order_fields:
                    with ui.column().classes('bg-white bg-opacity-70 rounded-lg p-3'):
                        ui.label(label).classes('text-sm font-medium text-blue-700')
                        
                        if key == 'total_amount' or label == 'Total Amount':
                            # Special formatting for currency
                            amount = order_data.get('total_net_amount', 0)
                            currency = order_data.get('currency', 'GBP')
                            value = format_currency(amount, currency)
                            ui.label(value).classes('text-lg font-semibold text-blue-900')
                        else:
                            value = order_data.get(key, '-')
                            if key == 'customer' and order_data.get('customer_name'):
                                # Show customer number and name
                                ui.label(str(value)).classes('text-blue-900 font-medium')
                                ui.label(order_data.get('customer_name', '')).classes('text-xs text-blue-700')
                            else:
                                ui.label(str(value)).classes('text-blue-900 font-medium')
            
            # Action buttons
            with ui.element('div').classes('bg-white bg-opacity-70 rounded-lg p-4 flex flex-wrap gap-3'):
                ui.button(
                    text='📋 Copy Details',
                    on_click=copy_to_clipboard
                ).classes('sky-button-success')
                
                ui.button(
                    text='📝 Create Billing Request',
                    on_click=create_billing_request
                ).classes('sky-button-primary')