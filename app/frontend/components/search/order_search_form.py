from nicegui import ui
from typing import Callable, Optional
import httpx
import asyncio
from app.frontend.components.ui.input_field import create_input_field
from app.frontend.components.ui.button import create_button
from app.frontend.components.ui.card import create_card

def create_order_search_form(on_search_result: Callable):
    """Create SAP sales order search form"""
    
    loading_indicator = ui.row().classes('hidden')
    search_input = None
    search_button = None

    def on_key_press(e):
        """Handle Enter key press in search input"""
        if e.key == 'Enter':
            asyncio.create_task(perform_search())

    # UI creation
    with create_card("Search SAP Sales Order").classes('max-w-2xl mx-auto'):
        ui.label('Enter a SAP sales order number to retrieve detailed order information.').classes('text-gray-600 mb-6')
        with ui.row().classes('gap-4 w-full items-end'):
            with ui.column().classes('flex-1'):
                def _create_input():
                    nonlocal search_input
                    search_input = create_input_field(
                        label="Sales Order Number",
                        placeholder="Enter SAP sales order number (e.g., 4500000001)",
                        helper_text="Press Enter to search or click the Search button"
                    )
                    search_input.on('keydown', on_key_press)
                _create_input()
            def _create_button():
                nonlocal search_button
                search_button = ui.button(
                    text='Search',
                    icon='search',
                    on_click=lambda: asyncio.create_task(perform_search())
                )
                search_button.classes('sky-button-primary mt-6')
            _create_button()
        with loading_indicator.classes('items-center gap-2 text-gray-600 mt-4'):
            ui.spinner(size='sm')
            ui.label('Searching...')
        with ui.element('div').classes('bg-gray-50 rounded-lg p-4 mt-6'):
            ui.label('🔗 SAP API Integration').classes('font-medium text-gray-700 mb-2')
            ui.label('Connected to SAP S/4HANA Cloud API for real-time sales order data.').classes('text-sm text-gray-600 mb-1')
            ui.html('<strong>Endpoint:</strong> <code class="bg-gray-200 px-1 py-0.5 rounded text-xs">API_SALES_ORDER_SRV</code>').classes('text-sm text-gray-600')

    async def perform_search():
        nonlocal search_input, search_button
        if search_input is None or search_button is None:
            ui.notify('Search form is not ready', type='warning')
            return
        order_number = search_input.value.strip()
        
        if not order_number:
            ui.notify('Please enter an order number', type='warning')
            return
        
        # Show loading state
        search_button.props('disabled')
        loading_indicator.classes(remove='hidden')
        
        try:
            # Call the backend API
            async with httpx.AsyncClient() as client:
                response = await client.get(f'/api/sap/orders/{order_number}')
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get('success'):
                        on_search_result(result.get('data'), None)
                        ui.notify('Order found successfully', type='positive')
                    else:
                        error_msg = result.get('errors', ['Order not found'])[0]
                        on_search_result(None, error_msg)
                        ui.notify(error_msg, type='negative')
                else:
                    error_msg = f'API error: {response.status_code}'
                    on_search_result(None, error_msg)
                    ui.notify(error_msg, type='negative')
                    
        except Exception as e:
            # Fallback to mock data for demo
            mock_data = {
                'order_number': order_number,
                'order_type': 'Standard Order (Mock)',
                'customer': '1000001',
                'customer_name': 'ABC Company Ltd',
                'status': 'Completed',
                'created_date': '2024-01-15',
                'total_net_amount': 15000.00,
                'currency': 'GBP',
                'sales_organization': '1000',
                'distribution_channel': '10',
                'division': '00',
                'requested_delivery_date': '2024-02-15',
                'payment_terms': 'Net 30'
            }
            on_search_result(mock_data, 'Note: Using mock data - SAP API may be restricted in this environment')
            ui.notify('Using mock data for demo', type='info')
        
        finally:
            if search_button is not None:
                search_button.props(remove='disabled')
            loading_indicator.classes(add='hidden')