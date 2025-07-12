from nicegui import ui
from typing import Optional, Callable

def create_modal(
    title: str,
    content_callback: Callable,
    show_close_button: bool = True,
    size: str = "md"
):
    """Create a modal dialog"""
    
    # Size classes
    size_classes = {
        'sm': 'max-w-sm',
        'md': 'max-w-md', 
        'lg': 'max-w-lg',
        'xl': 'max-w-xl'
    }
    
    with ui.dialog() as dialog, ui.card().classes(f'w-full {size_classes.get(size, "max-w-md")}'):
        # Modal header
        with ui.row().classes('w-full items-center justify-between mb-4'):
            ui.label(title).classes('text-lg font-semibold')
            if show_close_button:
                ui.button(icon='close', on_click=dialog.close).props('flat round')
        
        # Modal content
        content_callback()
    
    return dialog