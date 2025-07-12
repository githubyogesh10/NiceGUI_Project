from typing import List, Dict

# Base dropdown options used across the application
COMPANY_CODES = [
    {'value': '', 'label': 'Select company code'},
    {'value': '2000', 'label': '2000 - SKY UK LTD'},
    {'value': '2002', 'label': '2002 - Telecoms'},
    {'value': '2003', 'label': '2003 - Sky Healthcare Sch Ltd'},
    {'value': '2005', 'label': '2005 - SKY IN-HOME SERVICE'},
    {'value': '2008', 'label': '2008 - SKY CP LTD'},
]

REQUEST_TYPES = [
    {'value': '', 'label': 'Select request type'},
    {'value': 'INVOICE', 'label': 'Invoice'},
    {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
]

CURRENCIES = [
    {'value': '', 'label': 'Select currency'},
    {'value': 'GBP', 'label': 'GBP - British Pound'},
    {'value': 'EUR', 'label': 'EUR - Euro'},
    {'value': 'USD', 'label': 'USD - US Dollar'},
    {'value': 'CHF', 'label': 'CHF - Swiss Franc'},
    {'value': 'CZK', 'label': 'CZK - Czech Koruna'},
]

DEPARTMENTS = [
    {'value': '', 'label': 'Select department'},
    {'value': 'Finance', 'label': 'Finance'},
    {'value': 'Sales', 'label': 'Sales'},
    {'value': 'Marketing', 'label': 'Marketing'},
    {'value': 'Operations', 'label': 'Operations'},
]

REGIONS = [
    {'value': 'UK', 'label': 'UK&I'},
    {'value': 'DACH', 'label': 'DACH'},
    {'value': 'ITALY', 'label': 'Italy'},
]

# UK specific options
UK_REQUEST_TYPES = [
    {'value': '', 'label': 'Select type'},
    {'value': 'INVOICE', 'label': 'Invoice'},
    {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
    {'value': 'CONTRACT', 'label': 'Contract'},
    {'value': 'PRO_FORMA', 'label': 'Pro Forma'},
]

UK_COMPANIES = [
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
    {'value': '4962', 'label': '4962 - Sugar Films'},
]

UK_BILLING_REASONS = [
    {'value': '', 'label': 'Select reason'},
    {'value': 'multimedia', 'label': 'Multimedia Campaign / Non-Landmark Source System'},
    {'value': 'currency', 'label': 'Non-system currency'},
    {'value': 'timing_advance', 'label': 'Timing - Billing in Advance'},
    {'value': 'timing_frequency', 'label': 'Timing – Alternative Frequency (please state)'},
    {'value': 'media_revenues', 'label': 'Out of system media revenues (please state)'},
    {'value': 'customer_requirement', 'label': 'Customer specific requirement (please state and include confirmation from Media Governance Team)'},
    {'value': 'other', 'label': 'Other (please state and include confirmation from Media Governance Team)'},
]

# DACH specific options
DACH_REQUEST_TYPES = [
    {'value': '', 'label': 'Select type'},
    {'value': 'INVOICE', 'label': 'Invoice'},
    {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
    {'value': 'BARTER', 'label': 'Barter'},
    {'value': 'INSTALMENT', 'label': 'Instalment'},
]

DACH_CURRENCIES = [
    {'value': '', 'label': 'Select currency'},
    {'value': 'EUR', 'label': 'EUR'},
    {'value': 'USD', 'label': 'USD'},
    {'value': 'CHF', 'label': 'CHF'},
    {'value': 'GBP', 'label': 'GBP'},
    {'value': 'CZK', 'label': 'CZK'},
]

DACH_PAYMENT_TERMS = [
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
    {'value': '90_tage_3_skonto', 'label': '90 Tage 3% Skonto'},
]

DACH_COMPANIES = [
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
    {'value': '5686', 'label': '5686 - Sky Deutschland Interaction Center II GmbH'},
]

# Italy specific options
ITALY_REQUEST_TYPES = [
    {'value': '', 'label': 'Select type'},
    {'value': 'INVOICE', 'label': 'Invoice'},
    {'value': 'CREDIT_NOTE', 'label': 'Credit Note'},
]

ITALY_COMPANIES = [
    {'value': '', 'label': 'Select company'},
    {'value': '5001', 'label': '5001 - Sky Italia S.r.l.'},
    {'value': '5000', 'label': '5000 - Sky Italian Holdings S.p.A.'},
    {'value': '5005', 'label': '5005 - Sky Italia Network Service S.r.l.'},
    {'value': '5006', 'label': '5006 - Telepiù S.r.l.'},
    {'value': '5014', 'label': '5014 - Nuova Soc. Televisiva Italiana SRL'},
    {'value': '5015', 'label': '5015 - Vision Distribution S.p.A.'},
    {'value': '5016', 'label': '5016 - Digital Exchange S.r.l.'},
]

def get_dropdown_options_by_region(region: str) -> Dict[str, List[Dict[str, str]]]:
    """Get dropdown options for a specific region"""
    
    base_options = {
        'company_codes': COMPANY_CODES,
        'request_types': REQUEST_TYPES,
        'currencies': CURRENCIES,
        'departments': DEPARTMENTS,
        'regions': REGIONS
    }
    
    if region == 'UK':
        base_options.update({
            'uk_request_types': UK_REQUEST_TYPES,
            'uk_companies': UK_COMPANIES,
            'uk_billing_reasons': UK_BILLING_REASONS
        })
    elif region == 'DACH':
        base_options.update({
            'dach_request_types': DACH_REQUEST_TYPES,
            'dach_currencies': DACH_CURRENCIES,
            'dach_payment_terms': DACH_PAYMENT_TERMS,
            'dach_companies': DACH_COMPANIES
        })
    elif region == 'ITALY':
        base_options.update({
            'italy_request_types': ITALY_REQUEST_TYPES,
            'italy_companies': ITALY_COMPANIES
        })
    
    return base_options