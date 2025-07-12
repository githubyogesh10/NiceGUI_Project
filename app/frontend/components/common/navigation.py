from nicegui import ui

def create_navigation():
    """Create the navigation sidebar"""
    
    navigation_items = [
        {'id': 'home', 'label': 'Home', 'icon': 'home', 'path': '/'},
        {'id': 'billing', 'label': 'Create Billing Request', 'icon': 'description', 'path': '/billing'},
        {'id': 'search', 'label': 'Search Sales Order', 'icon': 'search', 'path': '/search'},
        {'id': 'about', 'label': 'About', 'icon': 'info', 'path': '/about'},
    ]
    
    with ui.column().classes('p-6 gap-2'):
        def make_on_click(path):
            def handler(_):
                ui.navigate.to(path)
            return handler

        for item in navigation_items:
            with ui.button(
                text=item['label'], 
                icon=item['icon'],
                on_click=make_on_click(item['path'])
            ).classes('sky-nav-item w-full justify-start'):
                pass