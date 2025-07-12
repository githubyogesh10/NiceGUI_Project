from typing import Dict, Optional
from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    """Currency conversion utilities"""
    
    def __init__(self):
        # Mock exchange rates - in production, these would come from an API
        self.exchange_rates = {
            'GBP': {
                'EUR': Decimal('1.17'),
                'USD': Decimal('1.27'),
                'CHF': Decimal('1.12'),
                'CZK': Decimal('30.5')
            },
            'EUR': {
                'GBP': Decimal('0.85'),
                'USD': Decimal('1.08'),
                'CHF': Decimal('0.96'),
                'CZK': Decimal('26.2')
            },
            'USD': {
                'GBP': Decimal('0.79'),
                'EUR': Decimal('0.93'),
                'CHF': Decimal('0.89'),
                'CZK': Decimal('24.3')
            },
            'CHF': {
                'GBP': Decimal('0.89'),
                'EUR': Decimal('1.04'),
                'USD': Decimal('1.12'),
                'CZK': Decimal('27.1')
            },
            'CZK': {
                'GBP': Decimal('0.033'),
                'EUR': Decimal('0.038'),
                'USD': Decimal('0.041'),
                'CHF': Decimal('0.037')
            }
        }
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Convert amount from one currency to another"""
        
        if from_currency == to_currency:
            return amount
        
        amount_decimal = Decimal(str(amount))
        
        # Get exchange rate
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            rate = self.exchange_rates[from_currency][to_currency]
            converted = amount_decimal * rate
            return float(converted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
        # If direct rate not available, return original amount
        return amount
    
    def get_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        """Get exchange rate between two currencies"""
        
        if from_currency == to_currency:
            return 1.0
        
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            return float(self.exchange_rates[from_currency][to_currency])
        
        return None
    
    def get_currency_symbol(self, currency: str) -> str:
        """Get currency symbol"""
        symbols = {
            'GBP': '£',
            'EUR': '€',
            'USD': '$',
            'CHF': 'CHF',
            'CZK': 'Kč'
        }
        return symbols.get(currency, currency)
    
    def format_currency(self, amount: float, currency: str, show_symbol: bool = True) -> str:
        """Format currency amount with symbol"""
        
        if show_symbol:
            symbol = self.get_currency_symbol(currency)
            return f"{symbol}{amount:,.2f}"
        else:
            return f"{amount:,.2f} {currency}"

# Global currency converter instance
currency_converter = CurrencyConverter()