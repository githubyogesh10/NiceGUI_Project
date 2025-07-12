from nicegui import ui
from typing import Dict, Any, Callable, Optional
from app.frontend.components.ui.input_field import create_input_field
from app.frontend.components.ui.select_field import create_select_field
from app.frontend.components.ui.card import create_card

def create_customer_details_form(
    form_data: Dict[str, Any],
    on_change: Callable,
    errors: Optional[Dict[str, str]] = None
):
    """Create customer details form step"""
    
    if errors is None:
        errors = {}
    
    with ui.column().classes('max-w-4xl mx-auto gap-6'):
        # Page header
        ui.label('Request & Customer Details').classes('text-2xl font-bold mb-2')
        ui.label('Please provide the basic request information and customer details.').classes('text-gray-600 mb-6')
        
        # Request Information Section
        with create_card("Request Information").classes('mb-6'):
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Requested By",
                        value=form_data.get('requested_by', ''),
                        placeholder="Enter your name",
                        required=True,
                        error=errors.get('requested_by'),
                        on_change=lambda e: on_change('requested_by', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Company Code",
                        options=[
                            {'value': '', 'label': 'Select company code'},
                            {'value': '2000', 'label': '2000 - SKY UK LTD'},
                            {'value': '2002', 'label': '2002 - Telecoms'},
                            {'value': '2003', 'label': '2003 - Sky Healthcare Sch Ltd'},
                            {'value': '2005', 'label': '2005 - SKY IN-HOME SERVICE'},
                            {'value': '2008', 'label': '2008 - SKY CP LTD'}
                        ],
                        value=form_data.get('company_code', ''),
                        required=True,
                        error=errors.get('company_code'),
                        on_change=lambda e: on_change('company_code', e.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Type of Request",
                        options=[
                            {'value': '', 'label': 'Select request type'},
                            {'value': 'INVOICE', 'label': 'Invoice'},
                            {'value': 'CREDIT_NOTE', 'label': 'Credit Note'}
                        ],
                        value=form_data.get('type_of_request', ''),
                        required=True,
                        error=errors.get('type_of_request'),
                        on_change=lambda e: on_change('type_of_request', e.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Department",
                        options=[
                            {'value': '', 'label': 'Select department'},
                            {'value': 'Finance', 'label': 'Finance'},
                            {'value': 'Sales', 'label': 'Sales'},
                            {'value': 'Marketing', 'label': 'Marketing'},
                            {'value': 'Operations', 'label': 'Operations'}
                        ],
                        value=form_data.get('department', ''),
                        required=True,
                        error=errors.get('department'),
                        on_change=lambda e: on_change('department', e.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="PO Number",
                        value=form_data.get('po_number', ''),
                        placeholder="Enter PO number (optional)",
                        error=errors.get('po_number'),
                        on_change=lambda e: on_change('po_number', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Currency",
                        options=[
                            {'value': '', 'label': 'Select currency'},
                            {'value': 'GBP', 'label': 'GBP - British Pound'},
                            {'value': 'EUR', 'label': 'EUR - Euro'},
                            {'value': 'USD', 'label': 'USD - US Dollar'}
                        ],
                        value=form_data.get('currency', ''),
                        required=True,
                        error=errors.get('currency'),
                        on_change=lambda e: on_change('currency', e.value)
                    )
        
        # Customer Information Section
        with create_card("Customer Information"):
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Customer Company Name",
                        value=form_data.get('customer_company_name', ''),
                        placeholder="Enter company name",
                        required=True,
                        error=errors.get('customer_company_name'),
                        on_change=lambda e: on_change('customer_company_name', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="SAP Customer Number",
                        value=form_data.get('sap_customer_number', ''),
                        placeholder="Enter SAP customer number",
                        helper_text="Will auto-populate customer data if valid",
                        error=errors.get('sap_customer_number'),
                        on_change=lambda e: on_change('sap_customer_number', e.sender.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Address",
                        value=form_data.get('address', ''),
                        placeholder="Enter customer address",
                        required=True,
                        error=errors.get('address'),
                        on_change=lambda e: on_change('address', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Post Code",
                        value=form_data.get('post_code', ''),
                        placeholder="Enter post code",
                        error=errors.get('post_code'),
                        on_change=lambda e: on_change('post_code', e.sender.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Country",
                        value=form_data.get('country', ''),
                        placeholder="Enter country",
                        required=True,
                        error=errors.get('country'),
                        on_change=lambda e: on_change('country', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Company Registration Number",
                        value=form_data.get('company_reg_no', ''),
                        placeholder="Enter registration number",
                        error=errors.get('company_reg_no'),
                        on_change=lambda e: on_change('company_reg_no', e.sender.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="VAT Number",
                        value=form_data.get('vat_number', ''),
                        placeholder="Enter VAT number",
                        error=errors.get('vat_number'),
                        on_change=lambda e: on_change('vat_number', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Contact Name",
                        value=form_data.get('contact_name', ''),
                        placeholder="Enter contact person name",
                        error=errors.get('contact_name'),
                        on_change=lambda e: on_change('contact_name', e.sender.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Client Email Address",
                        value=form_data.get('client_email', ''),
                        placeholder="Enter client email",
                        input_type="email",
                        error=errors.get('client_email'),
                        on_change=lambda e: on_change('client_email', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Payment Terms",
                        value=form_data.get('payment_terms', ''),
                        placeholder="Enter payment terms (if not standard)",
                        error=errors.get('payment_terms'),
                        on_change=lambda e: on_change('payment_terms', e.sender.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Invoice Header Text",
                        value=form_data.get('invoice_header_text', ''),
                        placeholder="Additional invoice text",
                        error=errors.get('invoice_header_text'),
                        on_change=lambda e: on_change('invoice_header_text', e.sender.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_input_field(
                        label="Sales & Distribution Channel",
                        value=form_data.get('sales_distribution_channel', ''),
                        placeholder="Enter S&D channel",
                        error=errors.get('sales_distribution_channel'),
                        on_change=lambda e: on_change('sales_distribution_channel', e.sender.value)
                    )
        
        # Customer validation status
        sap_customer_number = form_data.get('sap_customer_number', '')
        if sap_customer_number and len(sap_customer_number) >= 3:
            with ui.row().classes('items-center gap-2 text-green-600 mt-4'):
                ui.icon('check_circle').classes('text-green-600')
                ui.label('Customer validation in progress...').classes('text-sm font-medium')