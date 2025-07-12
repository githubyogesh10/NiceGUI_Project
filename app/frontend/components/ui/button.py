from nicegui import ui
from typing import Optional, Callable

def create_button(
    text: str,
    variant: str = "primary",
    icon: Optional[str] = None,
    on_click: Optional[Callable] = None,
    disabled: bool = False,
    loading: bool = False,
    full_width: bool = False
):
    """Create a styled button"""
    
    # Determine button classes based on variant
    button_classes = f'sky-button-{variant}'
    if full_width:
        button_classes += ' w-full'
    
    if loading:
        # Show loading spinner
        button_element = ui.button(icon='refresh', on_click=on_click).classes(button_classes)
        with button_element:
            ui.spinner(size='sm')
            ui.label(text).classes('ml-2')
    else:
        button_element = ui.button(
            text=text,
            icon=icon,
            on_click=on_click
        ).classes(button_classes)
        
        if disabled:
            button_element.disable()
    
    return button_element