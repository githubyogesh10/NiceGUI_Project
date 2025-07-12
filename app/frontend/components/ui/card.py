from nicegui import ui
from typing import Optional

def create_card(
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    padding: str = "p-6"
):
    """Create a styled card container"""
    
    card_container = ui.column().classes(f'sky-card {padding}')
    
    if title:
        with card_container:
            ui.label(title).classes('text-xl font-bold text-gray-900 mb-2')
            if subtitle:
                ui.label(subtitle).classes('text-gray-600 mb-4')
    
    return card_container