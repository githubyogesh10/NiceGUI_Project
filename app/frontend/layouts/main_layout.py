from nicegui import ui
from app.frontend.components.common.header import create_header
from app.frontend.components.common.navigation import create_navigation

def setup_main_layout():
    """Setup the main application layout"""
    
    # Create header first
    create_header()
    
    # Main container with proper layout
    with ui.element('div').classes('main-content'):
        # Content will be added by individual pages
        pass