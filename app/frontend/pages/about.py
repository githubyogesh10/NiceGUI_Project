from nicegui import ui

def about_page():
    """Create the about page"""
    
    with ui.column().classes('max-w-4xl mx-auto gap-8'):
        # Page header
        ui.label('About O2C Billing Portal').classes('text-3xl font-bold mb-8')
        
        # Main content
        with ui.element('div').classes('sky-card p-8'):
            # Enterprise solution section
            with ui.column().classes('mb-8'):
                ui.label('Enterprise Billing Solution').classes('text-xl font-semibold text-gray-900 mb-4')
                ui.label('The Order-to-Cash (O2C) Billing Portal streamlines manual billing requests with modern web technologies, Sky branding, and enterprise-grade security.').classes('text-gray-600 leading-relaxed')
            
            # Supported regions section
            with ui.column().classes('mb-8'):
                ui.label('Supported Regions').classes('text-xl font-semibold text-gray-900 mb-4')
                
                with ui.row().classes('gap-4'):
                    # UK&I
                    with ui.element('div').classes('bg-blue-50 rounded-lg p-4 flex-1'):
                        ui.label('UK&I').classes('font-semibold text-blue-800')
                        ui.label('United Kingdom & Ireland').classes('text-sm text-blue-700')
                    
                    # DACH
                    with ui.element('div').classes('bg-green-50 rounded-lg p-4 flex-1'):
                        ui.label('DACH').classes('font-semibold text-green-800')
                        ui.label('Deutschland, Austria, Switzerland').classes('text-sm text-green-700')
                    
                    # Italy
                    with ui.element('div').classes('bg-purple-50 rounded-lg p-4 flex-1'):
                        ui.label('Italy').classes('font-semibold text-purple-800')
                        ui.label('Italian market requirements').classes('text-sm text-purple-700')
            
            # Technology stack section
            with ui.element('div').classes('bg-gray-50 rounded-lg p-6'):
                ui.label('Technology Stack').classes('text-lg font-semibold text-gray-900 mb-4')
                
                with ui.row().classes('gap-8'):
                    with ui.column().classes('flex-1'):
                        tech_items = [
                            ('Frontend', 'NiceGUI 2.21.0'),
                            ('Backend', 'FastAPI + Python'),
                            ('Integration', 'SAP S/4HANA Cloud API'),
                            ('Version', '1.0.0 Demo')
                        ]
                        
                        for label, value in tech_items:
                            with ui.row().classes('justify-between py-1'):
                                ui.label(f'{label}:').classes('text-gray-600')
                                ui.label(value).classes('text-gray-900 font-medium')
            
            # Features section
            with ui.column().classes('mt-8'):
                ui.label('Key Features').classes('text-xl font-semibold text-gray-900 mb-4')
                
                features = [
                    'Multi-step form wizard with validation',
                    'Real-time SAP API integration',
                    'Regional-specific business rules',
                    'Responsive Sky-branded design',
                    'Line item calculations and totals',
                    'Draft saving and form persistence',
                    'Sales order search and lookup',
                    'Enterprise-grade architecture'
                ]
                
                with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-3'):
                    for feature in features:
                        with ui.row().classes('items-center gap-2'):
                            ui.icon('check_circle').classes('text-green-600')
                            ui.label(feature).classes('text-gray-700')
        
        # Contact section
        with ui.element('div').classes('sky-card p-6 bg-gradient-to-r from-blue-50 to-indigo-50'):
            ui.label('Support & Contact').classes('text-lg font-semibold text-blue-800 mb-3')
            ui.label('For technical support or feature requests, please contact the IT department.').classes('text-blue-700 mb-2')
            ui.label('© 2025 Sky Company - All rights reserved').classes('text-sm text-blue-600')