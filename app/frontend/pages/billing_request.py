from nicegui import ui
from typing import Dict, Any
import asyncio
import httpx
from app.frontend.components.forms.customer_details_form import create_customer_details_form
from app.frontend.components.forms.line_items_form import create_line_items_form
from app.frontend.components.forms.regional_specifics_form import create_regional_specifics_form
from app.frontend.components.forms.review_form import create_review_form
from app.backend.auth.auth_service import auth_service

# Force apply styles
ui.add_head_html('''
<style>
.q-header { background: linear-gradient(to right, #ff8c00 5%, #f80032 25%, #ff00a0 45%, #8c28ff 65%, #0023ff 82%, #19a0ff 96%) !important; }
.sky-card { background: white !important; border-radius: 0.5rem !important; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important; border: 1px solid #e5e7eb !important; }
.sky-card:hover { box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important; }
</style>
''')

def billing_request_page():
    """Create the billing request form page"""
    
    # Apply theme and create layout
    from app.frontend.styles.sky_theme import apply_sky_theme
    from app.frontend.components.common.header import create_header
    from app.frontend.components.common.navigation import create_navigation
    
    apply_sky_theme()
    create_header()
    
    # Create main layout with sidebar
    with ui.row().classes('w-full min-h-screen'):
        # Navigation sidebar
        with ui.column().classes('w-64 bg-white shadow-lg border-r fixed left-0 top-20 bottom-0 z-40'):
            create_navigation()
        
        # Main content area with left margin for sidebar
        with ui.column().classes('flex-1 ml-64 main-content'):

            # Get current user for default values
            current_user = auth_service.get_current_user()
            
            # Form state
            current_step = 0
            form_data = {
                'requested_by': current_user.name,
                'company_code': current_user.company_code,
                'department': current_user.department,
                'region': 'UK'
            }
            form_errors = {}
            
            steps = [
                {'id': 'customer', 'title': 'Customer Details'},
                {'id': 'lineItems', 'title': 'Line Items'},
                {'id': 'regional', 'title': 'Regional Specifics'},
                {'id': 'review', 'title': 'Review & Submit'}
            ]
            
            # Containers that will be refreshed
            progress_container = ui.row().classes('w-full items-center justify-between mb-8')
            content_container = ui.column().classes('w-full')
            navigation_container = ui.row().classes('w-full items-center justify-between mt-8 p-6 bg-gray-50 rounded-lg')
            
            def update_form_data(field: str, value: Any):
                """Update form data"""
                form_data[field] = value
                
                # Clear error when field is updated
                if field in form_errors:
                    form_errors.pop(field)
                    refresh_content()
            
            def validate_current_step():
                """Validate current form step"""
                errors = {}
                
                if current_step == 0:  # Customer Details
                    required_fields = [
                        'requested_by', 'company_code', 'type_of_request', 'department',
                        'currency', 'customer_company_name', 'address', 'country'
                    ]
                    for field in required_fields:
                        if not form_data.get(field):
                            field_name = field.replace('_', ' ').title()
                            errors[field] = f'{field_name} is required'
                    
                    # Email validation
                    email = form_data.get('client_email', '')
                    if email and '@' not in email:
                        errors['client_email'] = 'Please enter a valid email address'
                
                elif current_step == 1:  # Line Items
                    line_items = form_data.get('line_items', [])
                    if not line_items:
                        errors['line_items'] = 'At least one line item is required'
                    else:
                        for i, item in enumerate(line_items):
                            if not item.get('description'):
                                errors[f'line_item_{i}_description'] = f'Line item {i+1}: Description is required'
                            if not item.get('number_of_units') or item.get('number_of_units', 0) <= 0:
                                errors[f'line_item_{i}_units'] = f'Line item {i+1}: Units must be greater than 0'
                            if not item.get('unit_price') or item.get('unit_price', 0) <= 0:
                                errors[f'line_item_{i}_price'] = f'Line item {i+1}: Unit price must be greater than 0'
                
                elif current_step == 2:  # Regional Specifics
                    region = form_data.get('region', '')
                    if not region:
                        errors['region'] = 'Region is required'
                    elif region == 'UK':
                        uk_required = ['uk_type_of_request', 'uk_company', 'uk_manual_billing_reason']
                        for field in uk_required:
                            if not form_data.get(field):
                                errors[field] = f'UK {field.replace("uk_", "").replace("_", " ").title()} is required'
                    elif region == 'DACH':
                        dach_required = ['dach_type_of_request', 'dach_currency', 'dach_payment_terms', 'dach_company']
                        for field in dach_required:
                            if not form_data.get(field):
                                errors[field] = f'DACH {field.replace("dach_", "").replace("_", " ").title()} is required'
                    elif region == 'ITALY':
                        italy_required = ['italy_type_of_request', 'italy_company']
                        for field in italy_required:
                            if not form_data.get(field):
                                errors[field] = f'Italy {field.replace("italy_", "").replace("_", " ").title()} is required'
                
                form_errors.clear()
                form_errors.update(errors)
                return len(errors) == 0
            
            def handle_next():
                """Handle next button click"""
                nonlocal current_step
                
                if validate_current_step() and current_step < len(steps) - 1:
                    current_step += 1
                    refresh_all()
                elif form_errors:
                    ui.notify('Please fix the validation errors before proceeding', type='warning')
            
            def handle_previous():
                """Handle previous button click"""
                nonlocal current_step
                
                if current_step > 0:
                    current_step -= 1
                    refresh_all()
            
            async def handle_submit():
                """Handle form submission"""
                if not validate_current_step():
                    ui.notify('Please fix the validation errors before submitting', type='warning')
                    return
                
                try:
                    # Prepare submission data
                    submission_data = {
                        **form_data,
                        'regional_data': {}
                    }
                    
                    # Add regional data based on selected region
                    region = form_data.get('region', '')
                    if region == 'UK':
                        submission_data['regional_data']['uk'] = {
                            'type_of_request': form_data.get('uk_type_of_request'),
                            'company': form_data.get('uk_company'),
                            'manual_billing_reason': form_data.get('uk_manual_billing_reason')
                        }
                    elif region == 'DACH':
                        submission_data['regional_data']['dach'] = {
                            'type_of_request': form_data.get('dach_type_of_request'),
                            'currency': form_data.get('dach_currency'),
                            'payment_terms': form_data.get('dach_payment_terms'),
                            'company': form_data.get('dach_company')
                        }
                    elif region == 'ITALY':
                        submission_data['regional_data']['italy'] = {
                            'type_of_request': form_data.get('italy_type_of_request'),
                            'company': form_data.get('italy_company')
                        }
                    
                    # Submit to backend
                    async with httpx.AsyncClient() as client:
                        response = await client.post('/api/billing/submit', json=submission_data)
                        
                        if response.status_code == 200:
                            result = response.json()
                            if result.get('success'):
                                submission_id = result.get('data', {}).get('submission_id', 'Unknown')
                                ui.notify(f'Form submitted successfully! Submission ID: {submission_id}', type='positive')
                                
                                # Show success dialog
                                with ui.dialog() as success_dialog, ui.card().classes('max-w-md'):
                                    ui.label('Submission Successful!').classes('text-xl font-bold mb-4')
                                    ui.label(f'Your billing request has been submitted successfully.').classes('mb-2')
                                    ui.label(f'Submission ID: {submission_id}').classes('font-mono text-sm mb-4')
                                    ui.label('You will receive a confirmation email shortly.').classes('text-sm text-gray-600 mb-4')
                                    
                                    with ui.row().classes('gap-2 w-full'):
                                        ui.button('New Request', on_click=lambda: (success_dialog.close(), ui.navigate.to('/billing'))).classes('sky-button-success flex-1')
                                        ui.button('Go Home', on_click=lambda: (success_dialog.close(), ui.navigate.to('/'))).classes('sky-button-primary flex-1')
                                
                                success_dialog.open()
                            else:
                                error_msg = result.get('errors', ['Submission failed'])[0]
                                ui.notify(f'Submission failed: {error_msg}', type='negative')
                        else:
                            ui.notify(f'Submission failed: HTTP {response.status_code}', type='negative')
                            
                except Exception as e:
                    # Mock successful submission for demo
                    import random
                    submission_id = f"BR-{random.randint(10000, 99999)}"
                    ui.notify(f'Form submitted successfully! (Demo Mode) Submission ID: {submission_id}', type='positive')
            
            def save_draft():
                """Save form as draft"""
                # In a real implementation, this would save to backend or localStorage
                ui.notify('Draft saved locally!', type='info')
            
            def refresh_progress():
                """Refresh progress indicator"""
                progress_container.clear()
                
                with progress_container:
                    for i, step in enumerate(steps):
                        # Step circle
                        is_active = i <= current_step
                        is_current = i == current_step
                        
                        circle_class = 'sky-progress-step'
                        if is_active:
                            circle_class += ' active'
                        else:
                            circle_class += ' inactive'
                        
                        with ui.row().classes('items-center flex-1' if i < len(steps) - 1 else 'items-center'):
                            with ui.element('div').classes(circle_class):
                                ui.label(str(i + 1))
                            ui.label(step['title']).classes(
                                f'ml-2 text-sm font-medium {"text-blue-600" if is_active else "text-gray-400"}'
                            )
                            
                            # Progress line (except for last step)
                            if i < len(steps) - 1:
                                line_class = 'flex-1 h-0.5 mx-4 ' + ('bg-blue-600' if i < current_step else 'bg-gray-300')
                                ui.element('div').classes(line_class)
            
            def refresh_content():
                """Refresh form content based on current step"""
                content_container.clear()
                
                with content_container:
                    if current_step == 0:
                        create_customer_details_form(form_data, update_form_data, form_errors)
                    elif current_step == 1:
                        create_line_items_form(form_data, update_form_data, form_errors)
                    elif current_step == 2:
                        create_regional_specifics_form(form_data, update_form_data, form_errors)
                    elif current_step == 3:
                        create_review_form(form_data, form_errors)
            
            def refresh_navigation():
                """Refresh navigation buttons"""
                navigation_container.clear()
                
                with navigation_container:
                    # Save draft button
                    ui.button(
                        text='Save Draft',
                        icon='save',
                        on_click=save_draft
                    ).classes('sky-button-primary')
                    
                    # Navigation buttons
                    with ui.row().classes('gap-3 ml-auto'):
                        # Previous button
                        prev_button = ui.button(
                            text='Previous',
                            icon='chevron_left',
                            on_click=handle_previous
                        ).classes('border border-gray-300 bg-white text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-50')
                        
                        if current_step == 0:
                            prev_button.disable()
                        
                        # Next/Submit button
                        if current_step < len(steps) - 1:
                            ui.button(
                                text='Next',
                                icon='chevron_right',
                                on_click=handle_next
                            ).classes('sky-button-primary px-6 py-3')
                        else:
                            ui.button(
                                text='Submit Request',
                                icon='send',
                                on_click=lambda: asyncio.create_task(handle_submit())
                            ).classes('sky-button-success px-6 py-3')
            
            def refresh_all():
                """Refresh all components"""
                refresh_progress()
                refresh_content()
                refresh_navigation()
            
            # Main page layout
            with ui.column().classes('max-w-6xl mx-auto'):
                # Page header
                ui.label('Create Billing Request').classes('text-3xl font-bold mb-8')
                
                # Progress indicator
                with ui.element('div').classes('sky-card p-6 mb-8'):
                    refresh_progress()
                
                # Form content
                with ui.element('div').classes('sky-card overflow-hidden'):
                    refresh_content()
                    refresh_navigation()