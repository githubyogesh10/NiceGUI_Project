from nicegui import ui
from typing import List, Dict, Optional, Callable

def create_select_field(
    label: str,
    options: List[Dict[str, str]],
    value: str = "",
    required: bool = False,
    error: Optional[str] = None,
    helper_text: Optional[str] = None,
    on_change: Optional[Callable] = None,
    disabled: bool = False
):
    """Create a styled select field with label and validation"""
    
    with ui.column().classes('sky-form-group'):
        # Label
        label_text = label
        if required:
            label_text += " *"
        ui.label(label_text).classes('sky-label')
        
        # Select field
        select_classes = 'sky-select'
        if error:
            select_classes += ' error'
        
        # Convert options to the format expected by NiceGUI
        select_options = {opt['value']: opt['label'] for opt in options}
        
        select_element = ui.select(
            options=select_options,
            value=value if value else None
        ).classes(select_classes)
        
        if disabled:
            select_element.disable()
        
        if on_change:
            select_element.on('change', on_change)
        
        # Error message
        if error:
            ui.label(error).classes('sky-error')
        
        # Helper text
        if helper_text and not error:
            ui.label(helper_text).classes('text-xs text-gray-500 mt-1')
    
    return select_element