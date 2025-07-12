from nicegui import ui
from app.backend.auth.auth_service import auth_service

def create_header():
    """Create the main application header"""
    
    # Get current user (mock for now)
    current_user = auth_service.get_current_user()
    
    # Create fixed header
    with ui.header().classes('sky-header fixed top-0 left-0 right-0 z-50'):
        with ui.row().classes('w-full items-center justify-between px-6'):
            # Left side - Title
            ui.label('O2C Billing Portal').classes('text-2xl font-bold text-white')
            
            # Right side - User info
            with ui.row().classes('items-center gap-4'):
                if current_user:
                    with ui.column().classes('text-right text-white'):
                        ui.label(current_user.name).classes('text-sm font-medium')
                        ui.label(current_user.email).classes('text-xs opacity-90')
                    
                    with ui.element('div').classes('bg-white bg-opacity-20 px-4 py-2 rounded-lg flex items-center gap-2'):
                        ui.icon('person').classes('text-white')
                        ui.label('Demo Mode').classes('text-sm font-medium text-white')