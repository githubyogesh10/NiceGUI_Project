from nicegui import ui
from typing import Dict, Any, Callable, Optional

def create_review_form(form_data: Dict[str, Any], errors: Optional[Dict[str, str]] = None):
    """Create review and submit form step"""
    
    if errors is None:
        errors = {}
    
    def format_currency(amount: float, currency: str = 'GBP') -> str:
        """Format currency amount"""
        currency_symbols = {'GBP': '£', 'EUR': '€', 'USD': '$', 'CHF': 'CHF', 'CZK': 'CZK'}
        symbol = currency_symbols.get(currency, currency)
        return f"{symbol}{amount:,.2f}"
    
    def calculate_totals():
        """Calculate totals from line items"""
        line_items = form_data.get('line_items', [])
        total_net = sum(float(item.get('net_amount', 0)) for item in line_items)
        total_gross = sum(float(item.get('gross_amount', 0)) for item in line_items)
        total_commission = sum(float(item.get('commission_value', 0)) for item in line_items)
        
        return {
            'net_amount': total_net,
            'gross_amount': total_gross,
            'commission': total_commission
        }
    
    def get_regional_data_summary():
        """Get regional data summary based on selected region"""
        region = form_data.get('region', '')
        regional_data = {}
        
        if region == 'UK':
            regional_data = {
                'Type of Request': form_data.get('uk_type_of_request', ''),
                'Company': form_data.get('uk_company', ''),
                'Manual Billing Reason': form_data.get('uk_manual_billing_reason', '')
            }
        elif region == 'DACH':
            regional_data = {
                'Type of Request': form_data.get('dach_type_of_request', ''),
                'Currency': form_data.get('dach_currency', ''),
                'Payment Terms': form_data.get('dach_payment_terms', ''),
                'Company': form_data.get('dach_company', '')
            }
        elif region == 'ITALY':
            regional_data = {
                'Type of Request': form_data.get('italy_type_of_request', ''),
                'Company': form_data.get('italy_company', '')
            }
        
        return regional_data
    
    def is_form_valid():
        """Check if form is valid for submission"""
        required_fields = [
            'requested_by', 'company_code', 'type_of_request', 'currency',
            'customer_company_name', 'address', 'country'
        ]
        
        for field in required_fields:
            if not form_data.get(field):
                return False
        
        line_items = form_data.get('line_items', [])
        if not line_items:
            return False
        
        for item in line_items:
            if not item.get('description') or not item.get('number_of_units') or not item.get('unit_price'):
                return False
        
        return len(errors) == 0
    
    with ui.column().classes('max-w-4xl mx-auto gap-6'):
        # Page header
        ui.label('Review & Submit').classes('text-2xl font-bold mb-2')
        ui.label('Please review all information before submitting your billing request.').classes('text-gray-600 mb-6')
        
        # Validation status
        is_valid = is_form_valid()
        status_class = 'sky-alert-success' if is_valid else 'sky-alert-error'
        status_icon = 'check_circle' if is_valid else 'error'
        status_color = 'text-green-600' if is_valid else 'text-red-600'
        status_text = 'Form validation passed' if is_valid else 'Please fix validation errors before submitting'
        
        with ui.element('div').classes(f'sky-alert {status_class}'):
            with ui.row().classes('items-center gap-2'):
                ui.icon(status_icon).classes(status_color)
                ui.label(status_text).classes('font-medium')
            
            if not is_valid and errors:
                with ui.column().classes('mt-2 text-sm'):
                    ui.label('Please check the following sections:')
                    with ui.element('ul').classes('list-disc list-inside mt-1'):
                        for field in errors.keys():
                            field_name = field.replace('_', ' ').title()
                            with ui.element('li'):
                                ui.label(field_name)
                            
        
        # Request Summary
        with ui.element('div').classes('sky-card p-6 mb-6'):
            ui.label('Request Summary').classes('text-lg font-semibold text-sky-primary mb-4')
            
            with ui.row().classes('gap-8 w-full'):
                # Request Details
                with ui.column().classes('flex-1'):
                    ui.label('Request Details').classes('font-medium text-gray-700 mb-3')
                    
                    request_fields = [
                        ('Requested By', 'requested_by'),
                        ('Company Code', 'company_code'),
                        ('Type', 'type_of_request'),
                        ('Department', 'department'),
                        ('PO Number', 'po_number'),
                        ('Currency', 'currency')
                    ]
                    
                    for label, key in request_fields:
                        value = form_data.get(key, '-')
                        with ui.row().classes('justify-between py-1 border-b border-gray-100'):
                            ui.label(f'{label}:').classes('font-medium text-gray-600')
                            ui.label(str(value)).classes('text-gray-900')
                
                # Customer Details
                with ui.column().classes('flex-1'):
                    ui.label('Customer Details').classes('font-medium text-gray-700 mb-3')
                    
                    customer_fields = [
                        ('Company', 'customer_company_name'),
                        ('SAP Number', 'sap_customer_number'),
                        ('Address', 'address'),
                        ('Country', 'country'),
                        ('VAT Number', 'vat_number'),
                        ('Contact', 'contact_name')
                    ]
                    
                    for label, key in customer_fields:
                        value = form_data.get(key, '-')
                        with ui.row().classes('justify-between py-1 border-b border-gray-100'):
                            ui.label(f'{label}:').classes('font-medium text-gray-600')
                            ui.label(str(value)).classes('text-gray-900')
        
        # Line Items Summary
        line_items = form_data.get('line_items', [])
        if line_items:
            with ui.element('div').classes('sky-card p-6 mb-6'):
                ui.label(f'Line Items ({len(line_items)})').classes('text-lg font-semibold text-sky-primary mb-4')
                
                with ui.element('div').classes('overflow-x-auto'):
                    with ui.element('table').classes('sky-table'):
                        # Table header
                        with ui.element('thead'):
                            with ui.element('tr').classes('bg-gray-50'):
                                headers = ['Description', 'Units', 'Unit Price', 'Net Amount', 'Commission', 'VAT %', 'Gross Amount']
                                for header in headers:
                                    with ui.element('th').classes('text-sm font-semibold text-gray-700 px-3 py-2'):
                                        ui.label(header)
                        # Table body
                        with ui.element('tbody'):
                            currency = form_data.get('currency', 'GBP')
                            for item in line_items:
                                with ui.element('tr'):
                                    with ui.element('td').classes('px-3 py-2 text-sm'):
                                        ui.label(item.get('description', '-'))
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(str(item.get('number_of_units', 0)))
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(format_currency(item.get('unit_price', 0), currency))
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(format_currency(item.get('net_amount', 0), currency))
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(format_currency(item.get('commission_value', 0), currency))
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(f"{item.get('vat_percent', 0)}%")
                                    with ui.element('td').classes('px-3 py-2 text-sm text-center'):
                                        ui.label(format_currency(item.get('gross_amount', 0), currency))

                        # Table footer with totals
                        totals = calculate_totals()
                        with ui.element('tfoot'):
                            with ui.element('tr').classes('bg-gray-100 font-semibold'):
                                with ui.element('td').classes('px-3 py-2 text-right').props('colspan="3"'):
                                    ui.label('Totals:')
                                with ui.element('td').classes('px-3 py-2 text-center'):
                                    ui.label(format_currency(totals['net_amount'], currency))
                                with ui.element('td').classes('px-3 py-2 text-center'):
                                    ui.label(format_currency(totals['commission'], currency))
                                with ui.element('td').classes('px-3 py-2'):
                                    ui.label('')  # VAT % column
                                with ui.element('td').classes('px-3 py-2 text-center'):
                                    ui.label(format_currency(totals['gross_amount'], currency))

        # Regional Information
        region = form_data.get('region', '')
        regional_data = get_regional_data_summary()
        
        if region and regional_data:
            with ui.element('div').classes('sky-card p-6 mb-6'):
                ui.label(f'Regional Specifics - {region}').classes('text-lg font-semibold text-sky-primary mb-4')
                
                for label, value in regional_data.items():
                    if value:
                        with ui.row().classes('justify-between py-1 border-b border-gray-100'):
                            ui.label(f'{label}:').classes('font-medium text-gray-600')
                            ui.label(str(value)).classes('text-gray-900')
        
        # Final confirmation
        with ui.element('div').classes('bg-gradient-to-r from-yellow-50 to-yellow-100 border border-yellow-300 rounded-lg p-6'):
            with ui.row().classes('items-start gap-3'):
                ui.icon('warning').classes('text-yellow-600 mt-1 flex-shrink-0')
                with ui.column():
                    ui.label('Before submitting').classes('font-medium text-yellow-800 mb-2')
                    ui.label('Please ensure all information is correct. Once submitted, this request will be processed and sent to the billing system. You will receive a confirmation email with the submission details.').classes('text-sm text-yellow-700')