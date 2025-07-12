from typing import List, Dict, Any
from app.backend.models.masterdata import DropdownOptions, RegionConfig, CompanyData, MasterDataResponse
from app.backend.models.common import SelectOption

class MasterDataService:
    
    def get_dropdown_options(self) -> DropdownOptions:
        """Get all dropdown options for the application"""
        return DropdownOptions(
            company_codes=self._get_company_codes(),
            request_types=self._get_request_types(),
            currencies=self._get_currencies(),
            departments=self._get_departments(),
            regions=self._get_regions(),
            uk_companies=self._get_uk_companies(),
            uk_request_types=self._get_uk_request_types(),
            uk_billing_reasons=self._get_uk_billing_reasons(),
            dach_companies=self._get_dach_companies(),
            dach_request_types=self._get_dach_request_types(),
            dach_currencies=self._get_dach_currencies(),
            dach_payment_terms=self._get_dach_payment_terms(),
            italy_companies=self._get_italy_companies(),
            italy_request_types=self._get_italy_request_types()
        )
    
    def _get_company_codes(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select company code"),
            SelectOption(value="2000", label="2000 - SKY UK LTD"),
            SelectOption(value="2002", label="2002 - Telecoms"),
            SelectOption(value="2003", label="2003 - Sky Healthcare Sch Ltd"),
            SelectOption(value="2005", label="2005 - SKY IN-HOME SERVICE"),
            SelectOption(value="2008", label="2008 - SKY CP LTD"),
        ]
    
    def _get_request_types(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select request type"),
            SelectOption(value="INVOICE", label="Invoice"),
            SelectOption(value="CREDIT_NOTE", label="Credit Note"),
        ]
    
    def _get_currencies(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select currency"),
            SelectOption(value="GBP", label="GBP - British Pound"),
            SelectOption(value="EUR", label="EUR - Euro"),
            SelectOption(value="USD", label="USD - US Dollar"),
        ]
    
    def _get_departments(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select department"),
            SelectOption(value="Finance", label="Finance"),
            SelectOption(value="Sales", label="Sales"),
            SelectOption(value="Marketing", label="Marketing"),
            SelectOption(value="Operations", label="Operations"),
        ]
    
    def _get_regions(self) -> List[SelectOption]:
        return [
            SelectOption(value="UK", label="UK&I"),
            SelectOption(value="DACH", label="DACH"),
            SelectOption(value="ITALY", label="Italy"),
        ]
    
    def _get_uk_companies(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select company"),
            SelectOption(value="1008", label="1008 - S.A.T.V PUBLISHING (PREV. 4130)"),
            SelectOption(value="2000", label="2000 - SKY UK LTD"),
            SelectOption(value="2002", label="2002 - Telecoms"),
            SelectOption(value="2003", label="2003 - Sky Healthcare Sch Ltd"),
            SelectOption(value="2005", label="2005 - SKY IN-HOME SERVICE (PREV. 7000)"),
            SelectOption(value="2008", label="2008 - SKY CP LTD (PREV. 4970)"),
            SelectOption(value="2015", label="2015 - THE CLOUD NETWORKS (PREV. 4930)"),
            SelectOption(value="2017", label="2017 - SKY SNI LTD (PREV 4940)"),
            SelectOption(value="2019", label="2019 - Sky SNI Operations"),
            SelectOption(value="2031", label="2031 - Sky Studios (PREV. 4951)"),
            SelectOption(value="2033", label="2033 - CYMRU INTERNATIONAL (PREV. 4954)"),
            SelectOption(value="2050", label="2050 - NBCU"),
            SelectOption(value="2200", label="2200 Neos Ventures"),
            SelectOption(value="3000", label="3000 - SKY SUBSCRIBER SERVICES"),
            SelectOption(value="3001", label="3001 - IRISH BRANCH OF SSSL"),
            SelectOption(value="3070", label="3070 - SKY INTERNATIONAL AG (PREV. 5219)"),
            SelectOption(value="4900", label="4900 - SKY IQ"),
            SelectOption(value="5200", label="5200 - INT CHANNEL PACK DISTRIBUTION"),
            SelectOption(value="4962", label="4962 - Sugar Films"),
        ]
    
    def _get_uk_request_types(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select type"),
            SelectOption(value="INVOICE", label="Invoice"),
            SelectOption(value="CREDIT_NOTE", label="Credit Note"),
            SelectOption(value="CONTRACT", label="Contract"),
            SelectOption(value="PRO_FORMA", label="Pro Forma"),
        ]
    
    def _get_uk_billing_reasons(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select reason"),
            SelectOption(value="multimedia", label="Multimedia Campaign / Non-Landmark Source System"),
            SelectOption(value="currency", label="Non-system currency"),
            SelectOption(value="timing_advance", label="Timing - Billing in Advance"),
            SelectOption(value="timing_frequency", label="Timing – Alternative Frequency (please state)"),
            SelectOption(value="media_revenues", label="Out of system media revenues (please state)"),
            SelectOption(value="customer_requirement", label="Customer specific requirement (please state and include confirmation from Media Governance Team)"),
            SelectOption(value="other", label="Other (please state and include confirmation from Media Governance Team)"),
        ]
    
    def _get_dach_companies(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select company"),
            SelectOption(value="5616", label="5616 - Sky Deutschland GmbH"),
            SelectOption(value="5618", label="5618 - Sky DE Verwaltung GmbH"),
            SelectOption(value="5626", label="5626 - SCAS Satellite"),
            SelectOption(value="5633", label="5633 - Premiere Win"),
            SelectOption(value="5639", label="5639 - Sky Hotel Entertainment GmbH"),
            SelectOption(value="5648", label="5648 - Sky Deutschland Fernsehen GmbH & Co. KG"),
            SelectOption(value="5648_cz", label="5648 (CZ) - Sky Deutschland Fernsehen GmbH & Co. KG CZ"),
            SelectOption(value="5648_at", label="5648 (AT) - Sky Deutschland Fernsehen GmbH & Co. KG"),
            SelectOption(value="5649", label="5649 - Sky Österreich Fernsehen GmbH"),
            SelectOption(value="5649_cz", label="5649 (CZ) - Sky Österreich Fernsehen GmbH CZ"),
            SelectOption(value="5650", label="5650 - NBC Universal Global Networks Deutschland GmbH"),
            SelectOption(value="5658", label="5658 - Sky Deutschland Service Center GmbH"),
            SelectOption(value="5668", label="5668 - Sky Österreich Verwaltung GmbH"),
            SelectOption(value="5670", label="5670 - Sky Deutschland Customer Center GmbH"),
            SelectOption(value="5681", label="5681 - Sky Media GmbH"),
            SelectOption(value="5682", label="5682 - Sky German Holding"),
            SelectOption(value="5684", label="5684 - Sky Switzerland SA"),
            SelectOption(value="5685", label="5685 - Sky Deutschland Interaction Center I GmbH"),
            SelectOption(value="5686", label="5686 - Sky Deutschland Interaction Center II GmbH"),
        ]
    
    def _get_dach_request_types(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select type"),
            SelectOption(value="INVOICE", label="Invoice"),
            SelectOption(value="CREDIT_NOTE", label="Credit Note"),
            SelectOption(value="BARTER", label="Barter"),
            SelectOption(value="INSTALMENT", label="Instalment"),
        ]
    
    def _get_dach_currencies(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select currency"),
            SelectOption(value="EUR", label="EUR"),
            SelectOption(value="USD", label="USD"),
            SelectOption(value="CHF", label="CHF"),
            SelectOption(value="GBP", label="GBP"),
            SelectOption(value="CZK", label="CZK"),
        ]
    
    def _get_dach_payment_terms(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select terms"),
            SelectOption(value="prepaid", label="Prepaid"),
            SelectOption(value="immediate", label="Immediate"),
            SelectOption(value="7_tage", label="7 Tage"),
            SelectOption(value="14_tage_c4", label="14 Tage (C4)"),
            SelectOption(value="15_tage", label="15 Tage"),
            SelectOption(value="30_tage_c8", label="30 Tage (C8)"),
            SelectOption(value="60_tage", label="60 Tage"),
            SelectOption(value="90_tage", label="90 Tage"),
            SelectOption(value="barter_zbar", label="Barter (ZBAR)"),
            SelectOption(value="10_tage_2_skonto", label="10 Tage 2% Skonto"),
            SelectOption(value="10_tage_3_skonto", label="10 Tage 3% Skonto"),
            SelectOption(value="14_tage_2_skonto", label="14 Tage 2% Skonto"),
            SelectOption(value="14_tage_3_skonto", label="14 Tage 3% Skonto"),
            SelectOption(value="30_tage_3_skonto", label="30 Tage 3% Skonto"),
            SelectOption(value="30_tage_4_skonto", label="30 Tage 4% Skonto"),
            SelectOption(value="60_tage_2_skonto", label="60 Tage 2% Skonto"),
            SelectOption(value="70_tage_3_skonto", label="70 Tage 3% Skonto"),
            SelectOption(value="90_tage_3_skonto", label="90 Tage 3% Skonto"),
        ]
    
    def _get_italy_companies(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select company"),
            SelectOption(value="5001", label="5001 - Sky Italia S.r.l."),
            SelectOption(value="5000", label="5000 - Sky Italian Holdings S.p.A."),
            SelectOption(value="5005", label="5005 - Sky Italia Network Service S.r.l."),
            SelectOption(value="5006", label="5006 - Telepiù S.r.l."),
            SelectOption(value="5014", label="5014 - Nuova Soc. Televisiva Italiana SRL"),
            SelectOption(value="5015", label="5015 - Vision Distribution S.p.A."),
            SelectOption(value="5016", label="5016 - Digital Exchange S.r.l."),
        ]
    
    def _get_italy_request_types(self) -> List[SelectOption]:
        return [
            SelectOption(value="", label="Select type"),
            SelectOption(value="INVOICE", label="Invoice"),
            SelectOption(value="CREDIT_NOTE", label="Credit Note"),
        ]

# Global service instance
masterdata_service = MasterDataService()