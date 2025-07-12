from nicegui import ui
from typing import List, Dict, Any, Optional

def create_table(
    columns: List[Dict[str, Any]],
    data: List[Dict[str, Any]],
    title: Optional[str] = None
):
    """Create a styled data table"""
    
    with ui.column().classes('w-full'):
        if title:
            ui.label(title).classes('text-lg font-semibold mb-4')
        
        # Create table container
        with ui.element('div').classes('overflow-x-auto bg-white border border-gray-200 rounded-lg'):
            with ui.element('table').classes('sky-table'):
                # Table header
                with ui.element('thead'):
                    with ui.element('tr'):
                        for col in columns:
                            ui.element('th').props(f'innerHTML="{col['title']}"')

                # Table body
                with ui.element('tbody'):
                    for row in data:
                        with ui.element('tr'):
                            for col in columns:
                                cell_value = row.get(col['key'], '')
                                if col.get('render'):
                                    # Custom render function
                                    cell_content = col['render'](cell_value, row)
                                    ui.element('td').props(f'innerHTML="{str(cell_content)}"')
                                else:
                                    ui.element('td').props(f'innerHTML="{str(cell_value)}"')