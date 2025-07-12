from nicegui import ui
from typing import Dict, Any, Callable, List, Optional
import uuid
from app.frontend.components.ui.card import create_card
from app.frontend.components.ui.button import create_button

def create_line_items_form(
    form_data: Dict[str, Any],
    on_change: Callable,
    errors: Optional[Dict[str, str]] = None
):
    """Create line items form step"""
    
    if errors is None:
        errors = {}
    
    # Get line items from form data
    line_items = form_data.get('line_items', [])
    if not line_items:
        line_items = [{
            'id': str(uuid.uuid4()),
            'description': '',
            'sap_material_number': '',
            'wbs_code': '',
            'number_of_units': 0,
            'unit_price': 0,
            'net_amount': 0,
            'commission_value': 0,
            'vat_percent': 0,
            'gross_amount': 0
        }]
        on_change('line_items', line_items)
    
    def calculate_amounts(item_index: int):
        """Calculate net and gross amounts for a line item"""
        item = line_items[item_index]
        units = float(item.get('number_of_units', 0))
        unit_price = float(item.get('unit_price', 0))
        commission = float(item.get('commission_value', 0))
        vat_percent = float(item.get('vat_percent', 0))
        
        net_amount = units * unit_price
        vat_amount = net_amount * (vat_percent / 100)
        gross_amount = net_amount - commission + vat_amount
        
        item['net_amount'] = round(net_amount, 2)
        item['gross_amount'] = round(gross_amount, 2)
        
        on_change('line_items', line_items)
        refresh_table()
    
    def add_line_item():
        """Add a new line item"""
        new_item = {
            'id': str(uuid.uuid4()),
            'description': '',
            'sap_material_number': '',
            'wbs_code': '',
            'number_of_units': 0,
            'unit_price': 0,
            'net_amount': 0,
            'commission_value': 0,
            'vat_percent': 0,
            'gross_amount': 0
        }
        line_items.append(new_item)
        on_change('line_items', line_items)
        refresh_table()
    
    def remove_line_item(item_index: int):
        """Remove a line item"""
        if len(line_items) > 1:
            line_items.pop(item_index)
            on_change('line_items', line_items)
            refresh_table()
        else:
            ui.notify('At least one line item is required', type='warning')
    
    def calculate_totals():
        """Calculate total amounts"""
        total_net = sum(float(item.get('net_amount', 0)) for item in line_items)
        total_gross = sum(float(item.get('gross_amount', 0)) for item in line_items)
        total_commission = sum(float(item.get('commission_value', 0)) for item in line_items)
        
        return {
            'net_amount': round(total_net, 2),
            'gross_amount': round(total_gross, 2),
            'commission': round(total_commission, 2)
        }
    
    # Container for the table (will be refreshed)
    table_container = ui.column().classes('w-full')
    
    def refresh_table():
        """Refresh the line items table"""
        table_container.clear()
        
        with table_container:
            with ui.element('div').classes('overflow-x-auto bg-white border border-gray-200 rounded-lg mb-4'):
                with ui.element('table').classes('sky-table min-w-full'):
                    # Table header
                    with ui.element('thead'):
                        with ui.element('tr').classes('bg-gray-50'):
                            headers = [
                                'Description *', 'SAP Material', 'WBS Code', 'Units *',
                                'Unit Price *', 'Net Amount', 'Commission', 'VAT %',
                                'Gross Amount', 'Actions'
                            ]
                            for header in headers:
                                with ui.element('th').classes('text-xs font-semibold text-gray-700 px-3 py-2 text-center'):
                                    ui.label(header)
                    # Table body
                    with ui.element('tbody'):
                        for i, item in enumerate(line_items):
                            with ui.element('tr').classes('hover:bg-gray-50'):
                                # Description
                                with ui.element('td').classes('px-2 py-2'):
                                    desc_input = ui.input(
                                        value=item.get('description', ''),
                                        placeholder='Enter description'
                                    ).classes('w-full min-w-40 px-2 py-1 border rounded text-sm')
                                    desc_input.on('blur', lambda e, idx=i: setattr(line_items[idx], 'description', desc_input.value) or on_change('line_items', line_items))

                                # SAP Material Number
                                with ui.element('td').classes('px-2 py-2'):
                                    mat_input = ui.input(
                                        value=item.get('sap_material_number', ''),
                                        placeholder='Material #'
                                    ).classes('w-full min-w-24 px-2 py-1 border rounded text-sm')
                                    mat_input.on('blur', lambda e, idx=i: setattr(line_items[idx], 'sap_material_number', mat_input.value) or on_change('line_items', line_items))

                                # WBS Code
                                with ui.element('td').classes('px-2 py-2'):
                                    wbs_input = ui.input(
                                        value=item.get('wbs_code', ''),
                                        placeholder='WBS code'
                                    ).classes('w-full min-w-20 px-2 py-1 border rounded text-sm')
                                    wbs_input.on('blur', lambda e, idx=i: setattr(line_items[idx], 'wbs_code', wbs_input.value) or on_change('line_items', line_items))

                                # Number of Units
                                with ui.element('td').classes('px-2 py-2'):
                                    units_input = ui.number(
                                        value=item.get('number_of_units', 0),
                                        step=0.01,
                                        placeholder='0'
                                    ).classes('w-full min-w-20 px-2 py-1 border rounded text-sm')
                                    units_input.on('blur', lambda e, idx=i: (
                                        setattr(line_items[idx], 'number_of_units', units_input.value or 0),
                                        calculate_amounts(idx)
                                    ))
                                
                                # Unit Price
                                with ui.element('td').classes('px-2 py-2'):
                                    price_input = ui.number(
                                        value=item.get('unit_price', 0),
                                        step=0.01,
                                        placeholder='0.00'
                                    ).classes('w-full min-w-24 px-2 py-1 border rounded text-sm')
                                    price_input.on('blur', lambda e, idx=i: (
                                        setattr(line_items[idx], 'unit_price', price_input.value or 0),
                                        calculate_amounts(idx)
                                    ))
                                
                                # Net Amount (read-only)
                                with ui.element('td').classes('px-2 py-2'):
                                    ui.input(
                                        value=str(item.get('net_amount', 0.00))
                                    ).classes('w-full min-w-24 px-2 py-1 border rounded text-sm bg-gray-100').props('readonly')
                                
                                # Commission Value
                                with ui.element('td').classes('px-2 py-2'):
                                    comm_input = ui.number(
                                        value=item.get('commission_value', 0),
                                        step=0.01,
                                        placeholder='0.00'
                                    ).classes('w-full min-w-24 px-2 py-1 border rounded text-sm')
                                    comm_input.on('blur', lambda e, idx=i: (
                                        setattr(line_items[idx], 'commission_value', comm_input.value or 0),
                                        calculate_amounts(idx)
                                    ))
                                
                                # VAT Percent
                                with ui.element('td').classes('px-2 py-2'):
                                    vat_input = ui.number(
                                        value=item.get('vat_percent', 0),
                                        step=0.01,
                                        placeholder='0'
                                    ).classes('w-full min-w-16 px-2 py-1 border rounded text-sm')
                                    vat_input.on('blur', lambda e, idx=i: (
                                        setattr(line_items[idx], 'vat_percent', vat_input.value or 0),
                                        calculate_amounts(idx)
                                    ))
                                
                                # Gross Amount (read-only)
                                with ui.element('td').classes('px-2 py-2'):
                                    ui.input(
                                        value=str(item.get('gross_amount', 0.00))
                                    ).classes('w-full min-w-24 px-2 py-1 border rounded text-sm bg-gray-100').props('readonly')
                                
                                # Actions
                                with ui.element('td').classes('px-2 py-2 text-center'):
                                    remove_btn = ui.button(
                                        icon='delete',
                                        on_click=lambda e, idx=i: remove_line_item(idx)
                                    ).classes('bg-red-500 text-white px-2 py-1 rounded text-xs hover:bg-red-600')
                                    
                                    if len(line_items) == 1:
                                        remove_btn.disable()
                    
                    # Table footer with totals
                    totals = calculate_totals()
                    with ui.element('tfoot'):
                        with ui.element('tr').classes('bg-gray-100 font-semibold'):
                            with ui.element('td').classes('px-3 py-2 text-right').props('colspan="5"'):
                                ui.label('Totals:')
                            with ui.element('td').classes('px-3 py-2 text-center'):
                                ui.label(f"{totals['net_amount']:.2f}")
                            with ui.element('td').classes('px-3 py-2 text-center'):
                                ui.label(f"{totals['commission']:.2f}")
                            ui.element('td').classes('px-3 py-2')  # VAT % column
                            with ui.element('td').classes('px-3 py-2 text-center'):
                                ui.label(f"{totals['gross_amount']:.2f}")
                            with ui.element('td').classes('px-3 py-2'):
                                ui.label('')
                            ui.element('td').classes('px-3 py-2')  # Actions column

            # Add row button
            with ui.row().classes('gap-4 mt-4'):
                ui.button(
                    text='Add Line Item',
                    icon='add',
                    on_click=add_line_item
                ).classes('sky-button-success')
    
    with ui.column().classes('max-w-6xl mx-auto gap-6'):
        # Page header
        ui.label('Invoice Line Items').classes('text-2xl font-bold mb-2')
        ui.label('Add the line items for your billing request. All amounts will be calculated automatically.').classes('text-gray-600 mb-6')
        
        # Line items table
        refresh_table()
        
        # Summary card
        totals = calculate_totals()
        with ui.element('div').classes('bg-gradient-to-r from-blue-50 to-blue-100 border border-blue-200 rounded-lg p-6 mt-6'):
            with ui.row().classes('w-full items-center justify-between'):
                with ui.column():
                    ui.label('Invoice Summary').classes('text-lg font-semibold text-blue-800 mb-1')
                    ui.label(f'Total line items: {len(line_items)}').classes('text-sm text-blue-700')
                
                with ui.column().classes('text-right'):
                    ui.label('Total Net Amount').classes('text-sm text-blue-700')
                    ui.label(f'{totals["net_amount"]:.2f}').classes('text-2xl font-bold text-blue-800')
                    ui.label(f'Total Gross Amount: {totals["gross_amount"]:.2f}').classes('text-sm text-blue-700')