from nicegui import ui
from typing import Optional, Dict, Any
from app.frontend.components.search.order_search_form import create_order_search_form
from app.frontend.components.search.order_results import create_order_results

def order_search_page():
    """Create the order search page"""
    
    # Container for search results
    results_container = ui.column().classes('w-full')
    
    def handle_search_result(order_data: Optional[Dict[str, Any]], error_message: Optional[str]):
        """Handle search results"""
        results_container.clear()
        
        with results_container:
            create_order_results(order_data, error_message)
    
    with ui.column().classes('max-w-4xl mx-auto gap-8'):
        # Page header
        ui.label('Search SAP Sales Order').classes('text-3xl font-bold mb-2')
        ui.label('Search for existing sales orders and view their detailed information.').classes('text-gray-600 mb-8')
        
        # Search form
        create_order_search_form(handle_search_result)
        
        # Results area
        results_container