from nicegui import ui
from datetime import datetime

def home_page():
    """Create the home dashboard page"""
    
    def get_greeting():
        """Get time-based greeting"""
        hour = datetime.now().hour
        if hour < 12:
            return "Good morning"
        elif hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
    
    def navigate_to_billing():
        """Navigate to billing request page"""
        ui.navigate.to('/billing')
    
    def navigate_to_search():
        """Navigate to order search page"""
        ui.navigate.to('/search')
    
    with ui.column().classes('max-w-6xl mx-auto gap-8'):
        # Welcome section
        with ui.column().classes('text-center mb-8'):
            ui.label(f'{get_greeting()}!').classes('text-3xl font-bold text-gray-900 mb-4')
            ui.label('Welcome to the O2C Billing Portal').classes('text-xl text-gray-600')
            ui.label('What would you like to do today?').classes('text-gray-500 mt-2')
        
        # Quick actions
        with ui.row().classes('gap-6 justify-center w-full'):
            # Create billing request card
            with ui.element('div').classes('sky-card p-6 max-w-sm hover:shadow-lg transition-shadow cursor-pointer').on('click', navigate_to_billing):
                with ui.row().classes('items-center mb-4'):
                    ui.icon('description').classes('text-blue-600 text-4xl')
                    ui.label('Create Billing Request').classes('text-xl font-semibold text-gray-900 ml-3')
                
                ui.label('Create a new manual billing request with customer details, line items, and regional specifications.').classes('text-gray-600 mb-4')
                
                ui.button(
                    text='Get Started',
                    on_click=navigate_to_billing
                ).classes('sky-button-success w-full')
            
            # Search orders card
            with ui.element('div').classes('sky-card p-6 max-w-sm hover:shadow-lg transition-shadow cursor-pointer').on('click', navigate_to_search):
                with ui.row().classes('items-center mb-4'):
                    ui.icon('search').classes('text-blue-600 text-4xl')
                    ui.label('Search Sales Order').classes('text-xl font-semibold text-gray-900 ml-3')
                
                ui.label('Search for existing sales orders and view their details and billing status.').classes('text-gray-600 mb-4')
                
                ui.button(
                    text='Search Orders',
                    on_click=navigate_to_search
                ).classes('sky-button-primary w-full')
        
        # Recent activity section
        with ui.element('div').classes('bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-6 mt-8'):
            ui.label('Recent Activity').classes('text-lg font-semibold text-gray-900 mb-4')
            
            recent_items = [
                {'id': 'BR-001', 'status': 'Submitted', 'status_class': 'sky-badge-success'},
                {'id': 'BR-002', 'status': 'Draft', 'status_class': 'sky-badge-warning'},
                {'id': 'BR-003', 'status': 'Processing', 'status_class': 'sky-badge-info'}
            ]
            
            with ui.column().classes('gap-3'):
                for item in recent_items:
                    with ui.row().classes('items-center justify-between py-2 border-b border-gray-200 last:border-b-0'):
                        ui.label(f'Billing Request #{item["id"]}').classes('text-gray-700')
                        with ui.element('span').classes(f'sky-badge {item["status_class"]}'):
                            ui.label(item['status'])
        
        # Statistics section
        with ui.row().classes('gap-6 w-full mt-8'):
            stats = [
                {'title': 'Total Requests', 'value': '24', 'icon': 'description', 'color': 'blue'},
                {'title': 'This Month', 'value': '8', 'icon': 'calendar_today', 'color': 'green'},
                {'title': 'Pending', 'value': '3', 'icon': 'pending', 'color': 'yellow'},
                {'title': 'Completed', 'value': '21', 'icon': 'check_circle', 'color': 'green'}
            ]
            
            for stat in stats:
                with ui.element('div').classes('sky-card p-4 flex-1 text-center'):
                    ui.icon(stat['icon']).classes(f'text-{stat["color"]}-600 text-3xl mb-2')
                    ui.label(stat['value']).classes('text-2xl font-bold text-gray-900')
                    ui.label(stat['title']).classes('text-sm text-gray-600')