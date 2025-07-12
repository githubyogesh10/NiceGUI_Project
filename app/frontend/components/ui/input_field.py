from nicegui import ui
from typing import Optional, Callable

def create_input_field(
    label: str,
    value: str = "",
    placeholder: str = "",
    required: bool = False,
    error: Optional[str] = None,
    helper_text: Optional[str] = None,
    input_type: str = "text",
    on_change: Optional[Callable] = None,
    disabled: bool = False
):
    """Create a styled input field with label and validation"""
    
    with ui.column().classes('sky-form-group'):
        # Label
        label_text = label
        if required:
            label_text += " *"
        ui.label(label_text).classes('sky-label')
        
        # Input field
        input_classes = 'sky-input'
        if error:
            input_classes += ' error'
        
        if input_type == "email":
            input_element = ui.input(
                value=value,
                placeholder=placeholder,
                validation={'Email': lambda value: '@' in value}
            ).classes(input_classes)
        elif input_type == "number":
            input_element = ui.number(
                value=float(value) if value else None,
                placeholder=placeholder
            ).classes(input_classes)
        else:
            input_element = ui.input(
                value=value,
                placeholder=placeholder
            ).classes(input_classes)
        
        if disabled:
            input_element.disable()
        
        if on_change:
            input_element.on('blur', on_change)
        
        # Error message
        if error:
            ui.label(error).classes('sky-error')
        
        # Helper text
        if helper_text and not error:
            ui.label(helper_text).classes('text-xs text-gray-500 mt-1')
    
    return input_element