from nicegui import ui
from typing import Dict, Any, Callable, Optional
from app.frontend.components.ui.select_field import create_select_field
from app.frontend.components.ui.card import create_card

def create_regional_specifics_form(
    form_data: Dict[str, Any],
    on_change: Callable,
    errors: Optional[Dict[str, str]] = None
):
    """Create regional specifics form step"""
    
    if errors is None:
        errors = {}
    
    selected_region = form_data.get('region', 'UK')
    
    # Container for regional fields (will be refreshed when region changes)
    regional_container = ui.column().classes('w-full')
    
    def refresh_regional_fields():
        """Refresh regional specific fields based on selected region"""
        regional_container.clear()
        
        with regional_container:
            if selected_region == 'UK':
                create_uk_fields()
            elif selected_region == 'DACH':
                create_dach_fields()
            elif selected_region == 'ITALY':
                create_italy_fields()
    
    def create_uk_fields():
        """Create UK specific fields"""
        with create_card("UK&I Specific Fields").classes('mt-6'):
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Type of Request",
                        options=[
                            {'value': '', 'label': 'Select type'},
                            {'value': 'INVOICE', 'label': 'Invoice'},
                            {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
                            {'value': 'CONTRACT', 'label': 'Contract'},
                            {'value': 'PRO_FORMA', 'label': 'Pro Forma'}
                        ],
                        value=form_data.get('uk_type_of_request', ''),
                        required=True,
                        error=errors.get('uk_type_of_request'),
                        on_change=lambda e: on_change('uk_type_of_request', e.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Company",
                        options=[
                            {'value': '', 'label': 'Select company'},
                            {'value': '1008', 'label': '1008 - S.A.T.V PUBLISHING (PREV. 4130)'},
                            {'value': '2000', 'label': '2000 - SKY UK LTD'},
                            {'value': '2002', 'label': '2002 - Telecoms'},
                            {'value': '2003', 'label': '2003 - Sky Healthcare Sch Ltd'},
                            {'value': '2005', 'label': '2005 - SKY IN-HOME SERVICE (PREV. 7000)'},
                            {'value': '2008', 'label': '2008 - SKY CP LTD (PREV. 4970)'},
                            {'value': '2015', 'label': '2015 - THE CLOUD NETWORKS (PREV. 4930)'},
                            {'value': '2017', 'label': '2017 - SKY SNI LTD (PREV 4940)'},
                            {'value': '2019', 'label': '2019 - Sky SNI Operations'},
                            {'value': '2031', 'label': '2031 - Sky Studios (PREV. 4951)'},
                            {'value': '2033', 'label': '2033 - CYMRU INTERNATIONAL (PREV. 4954)'},
                            {'value': '2050', 'label': '2050 - NBCU'},
                            {'value': '2200', 'label': '2200 Neos Ventures'},
                            {'value': '3000', 'label': '3000 - SKY SUBSCRIBER SERVICES'},
                            {'value': '3001', 'label': '3001 - IRISH BRANCH OF SSSL'},
                            {'value': '3070', 'label': '3070 - SKY INTERNATIONAL AG (PREV. 5219)'},
                            {'value': '4900', 'label': '4900 - SKY IQ'},
                            {'value': '5200', 'label': '5200 - INT CHANNEL PACK DISTRIBUTION'},
                            {'value': '4962', 'label': '4962 - Sugar Films'}
                        ],
                        value=form_data.get('uk_company', ''),
                        required=True,
                        error=errors.get('uk_company'),
                        on_change=lambda e: on_change('uk_company', e.value)
                    )
            
            with ui.column().classes('w-full'):
                create_select_field(
                    label="Manual Billing Reason",
                    options=[
                        {'value': '', 'label': 'Select reason'},
                        {'value': 'multimedia', 'label': 'Multimedia Campaign / Non-Landmark Source System'},
                        {'value': 'currency', 'label': 'Non-system currency'},
                        {'value': 'timing_advance', 'label': 'Timing - Billing in Advance'},
                        {'value': 'timing_frequency', 'label': 'Timing – Alternative Frequency (please state)'},
                        {'value': 'media_revenues', 'label': 'Out of system media revenues (please state)'},
                        {'value': 'customer_requirement', 'label': 'Customer specific requirement (please state and include confirmation from Media Governance Team)'},
                        {'value': 'other', 'label': 'Other (please state and include confirmation from Media Governance Team)'}
                    ],
                    value=form_data.get('uk_manual_billing_reason', ''),
                    required=True,
                    error=errors.get('uk_manual_billing_reason'),
                    on_change=lambda e: on_change('uk_manual_billing_reason', e.value)
                )
    
    def create_dach_fields():
        """Create DACH specific fields"""
        with create_card("DACH Specific Fields").classes('mt-6'):
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Type of Request",
                        options=[
                            {'value': '', 'label': 'Select type'},
                            {'value': 'INVOICE', 'label': 'Invoice'},
                            {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
                            {'value': 'BARTER', 'label': 'Barter'},
                            {'value': 'INSTALMENT', 'label': 'Instalment'}
                        ],
                        value=form_data.get('dach_type_of_request', ''),
                        required=True,
                        error=errors.get('dach_type_of_request'),
                        on_change=lambda e: on_change('dach_type_of_request', e.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Currency",
                        options=[
                            {'value': '', 'label': 'Select currency'},
                            {'value': 'EUR', 'label': 'EUR'},
                            {'value': 'USD', 'label': 'USD'},
                            {'value': 'CHF', 'label': 'CHF'},
                            {'value': 'GBP', 'label': 'GBP'},
                            {'value': 'CZK', 'label': 'CZK'}
                        ],
                        value=form_data.get('dach_currency', ''),
                        required=True,
                        error=errors.get('dach_currency'),
                        on_change=lambda e: on_change('dach_currency', e.value)
                    )
            
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Payment Terms",
                        options=[
                            {'value': '', 'label': 'Select terms'},
                            {'value': 'prepaid', 'label': 'Prepaid'},
                            {'value': 'immediate', 'label': 'Immediate'},
                            {'value': '7_tage', 'label': '7 Tage'},
                            {'value': '14_tage_c4', 'label': '14 Tage (C4)'},
                            {'value': '15_tage', 'label': '15 Tage'},
                            {'value': '30_tage_c8', 'label': '30 Tage (C8)'},
                            {'value': '60_tage', 'label': '60 Tage'},
                            {'value': '90_tage', 'label': '90 Tage'},
                            {'value': 'barter_zbar', 'label': 'Barter (ZBAR)'},
                            {'value': '10_tage_2_skonto', 'label': '10 Tage 2% Skonto'},
                            {'value': '10_tage_3_skonto', 'label': '10 Tage 3% Skonto'},
                            {'value': '14_tage_2_skonto', 'label': '14 Tage 2% Skonto'},
                            {'value': '14_tage_3_skonto', 'label': '14 Tage 3% Skonto'},
                            {'value': '30_tage_3_skonto', 'label': '30 Tage 3% Skonto'},
                            {'value': '30_tage_4_skonto', 'label': '30 Tage 4% Skonto'},
                            {'value': '60_tage_2_skonto', 'label': '60 Tage 2% Skonto'},
                            {'value': '70_tage_3_skonto', 'label': '70 Tage 3% Skonto'},
                            {'value': '90_tage_3_skonto', 'label': '90 Tage 3% Skonto'}
                        ],
                        value=form_data.get('dach_payment_terms', ''),
                        required=True,
                        error=errors.get('dach_payment_terms'),
                        on_change=lambda e: on_change('dach_payment_terms', e.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Company",
                        options=[
                            {'value': '', 'label': 'Select company'},
                            {'value': '5616', 'label': '5616 - Sky Deutschland GmbH'},
                            {'value': '5618', 'label': '5618 - Sky DE Verwaltung GmbH'},
                            {'value': '5626', 'label': '5626 - SCAS Satellite'},
                            {'value': '5633', 'label': '5633 - Premiere Win'},
                            {'value': '5639', 'label': '5639 - Sky Hotel Entertainment GmbH'},
                            {'value': '5648', 'label': '5648 - Sky Deutschland Fernsehen GmbH & Co. KG'},
                            {'value': '5648_cz', 'label': '5648 (CZ) - Sky Deutschland Fernsehen GmbH & Co. KG CZ'},
                            {'value': '5648_at', 'label': '5648 (AT) - Sky Deutschland Fernsehen GmbH & Co. KG'},
                            {'value': '5649', 'label': '5649 - Sky Österreich Fernsehen GmbH'},
                            {'value': '5649_cz', 'label': '5649 (CZ) - Sky Österreich Fernsehen GmbH CZ'},
                            {'value': '5650', 'label': '5650 - NBC Universal Global Networks Deutschland GmbH'},
                            {'value': '5658', 'label': '5658 - Sky Deutschland Service Center GmbH'},
                            {'value': '5668', 'label': '5668 - Sky Österreich Verwaltung GmbH'},
                            {'value': '5670', 'label': '5670 - Sky Deutschland Customer Center GmbH'},
                            {'value': '5681', 'label': '5681 - Sky Media GmbH'},
                            {'value': '5682', 'label': '5682 - Sky German Holding'},
                            {'value': '5684', 'label': '5684 - Sky Switzerland SA'},
                            {'value': '5685', 'label': '5685 - Sky Deutschland Interaction Center I GmbH'},
                            {'value': '5686', 'label': '5686 - Sky Deutschland Interaction Center II GmbH'}
                        ],
                        value=form_data.get('dach_company', ''),
                        required=True,
                        error=errors.get('dach_company'),
                        on_change=lambda e: on_change('dach_company', e.value)
                    )
    
    def create_italy_fields():
        """Create Italy specific fields"""
        with create_card("Italy Specific Fields").classes('mt-6'):
            with ui.row().classes('gap-6 w-full'):
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Type of Request",
                        options=[
                            {'value': '', 'label': 'Select type'},
                            {'value': 'INVOICE', 'label': 'Invoice'},
                            {'value': 'CREDIT_NOTE', 'label': 'Credit Note'}
                        ],
                        value=form_data.get('italy_type_of_request', ''),
                        required=True,
                        error=errors.get('italy_type_of_request'),
                        on_change=lambda e: on_change('italy_type_of_request', e.value)
                    )
                
                with ui.column().classes('flex-1 min-w-0'):
                    create_select_field(
                        label="Company",
                        options=[
                            {'value': '', 'label': 'Select company'},
                            {'value': '5001', 'label': '5001 - Sky Italia S.r.l.'},
                            {'value': '5000', 'label': '5000 - Sky Italian Holdings S.p.A.'},
                            {'value': '5005', 'label': '5005 - Sky Italia Network Service S.r.l.'},
                            {'value': '5006', 'label': '5006 - Telepiù S.r.l.'},
                            {'value': '5014', 'label': '5014 - Nuova Soc. Televisiva Italiana SRL'},
                            {'value': '5015', 'label': '5015 - Vision Distribution S.p.A.'},
                            {'value': '5016', 'label': '5016 - Digital Exchange S.r.l.'}
                        ],
                        value=form_data.get('italy_company', ''),
                        required=True,
                        error=errors.get('italy_company'),
                        on_change=lambda e: on_change('italy_company', e.value)
                    )
    
    def get_regional_info():
        """Get information about the selected region"""
        region_info = {
            'UK': {
                'title': 'UK&I',
                'description': 'United Kingdom and Ireland billing requirements',
                'details': 'Please ensure all UK-specific compliance requirements are met.'
            },
            'DACH': {
                'title': 'DACH',
                'description': 'Deutschland, Austria, and Switzerland billing requirements',
                'details': 'Multiple currencies and payment terms are supported for this region.'
            },
            'ITALY': {
                'title': 'Italy',
                'description': 'Italian billing requirements and regulations',
                'details': 'Please ensure VAT compliance for Italian customers.'
            }
        }
        return region_info.get(selected_region, {
            'title': 'Region',
            'description': 'Select a region to see specific requirements',
            'details': ''
        })
    
    def on_region_change(new_region):
        """Handle region selection change"""
        nonlocal selected_region
        selected_region = new_region
        on_change('region', new_region)
        refresh_regional_fields()
    
    with ui.column().classes('max-w-4xl mx-auto gap-6'):
        # Page header
        ui.label('Regional Specifics').classes('text-2xl font-bold mb-2')
        ui.label('Select your region and provide region-specific information.').classes('text-gray-600 mb-6')
        
        # Region selection
        with create_card().classes('mb-6'):
            create_select_field(
                label="Region",
                options=[
                    {'value': 'UK', 'label': 'UK&I'},
                    {'value': 'DACH', 'label': 'DACH'},
                    {'value': 'ITALY', 'label': 'Italy'}
                ],
                value=selected_region,
                required=True,
                error=errors.get('region'),
                on_change=lambda e: on_region_change(e.value)
            )
        
        # Regional specific fields
        refresh_regional_fields()
        
        # Regional information
        regional_info = get_regional_info()
        with ui.element('div').classes('bg-gradient-to-r from-blue-50 to-blue-100 border border-blue-200 rounded-lg p-6 mt-6'):
            ui.label('Regional Information').classes('text-lg font-semibold text-blue-800 mb-2')
            with ui.column().classes('text-sm text-blue-700'):
                ui.label(f"{regional_info['title']}: {regional_info['description']}").classes('mb-2')
                if regional_info.get('details'):
                    ui.label(regional_info['details'])