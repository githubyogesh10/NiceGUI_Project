from typing import List, Dict, Any, Optional

def calculate_line_item_amounts(
    units: float,
    unit_price: float, 
    commission_value: float = 0.0,
    vat_percent: float = 0.0
) -> Dict[str, float]:
    """Calculate net and gross amounts for a line item"""
    
    net_amount = units * unit_price
    vat_amount = net_amount * (vat_percent / 100)
    gross_amount = net_amount - commission_value + vat_amount
    
    return {
        'net_amount': round(net_amount, 2),
        'vat_amount': round(vat_amount, 2),
        'gross_amount': round(gross_amount, 2)
    }

def calculate_totals(line_items: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate total amounts from line items"""
    
    total_net = sum(float(item.get('net_amount', 0)) for item in line_items)
    total_gross = sum(float(item.get('gross_amount', 0)) for item in line_items)
    total_commission = sum(float(item.get('commission_value', 0)) for item in line_items)
    total_vat = sum(
        float(item.get('net_amount', 0)) * float(item.get('vat_percent', 0)) / 100 
        for item in line_items
    )
    
    return {
        'total_net_amount': round(total_net, 2),
        'total_gross_amount': round(total_gross, 2),
        'total_commission': round(total_commission, 2),
        'total_vat': round(total_vat, 2),
        'item_count': len(line_items)
    }

def calculate_tax_amount(net_amount: float, tax_rate: float) -> float:
    """Calculate tax amount"""
    return round(net_amount * (tax_rate / 100), 2)

def calculate_discount_amount(
    original_amount: float, 
    discount_percent: float = 0.0,
    discount_amount: float = 0.0
) -> Dict[str, float]:
    """Calculate discount amount and final price"""
    
    if discount_percent > 0:
        discount_value = original_amount * (discount_percent / 100)
    else:
        discount_value = discount_amount
    
    final_amount = original_amount - discount_value
    
    return {
        'discount_value': round(discount_value, 2),
        'final_amount': round(final_amount, 2),
        'discount_percent': round((discount_value / original_amount) * 100, 2) if original_amount > 0 else 0
    }

def convert_currency(
    amount: float, 
    from_currency: str, 
    to_currency: str,
    exchange_rates: Optional[Dict[str, float]] = None
) -> float:
    """Convert amount between currencies"""
    
    # Mock exchange rates for demo
    if exchange_rates is None:
        exchange_rates = {
            'GBP_EUR': 1.17,
            'GBP_USD': 1.27,
            'EUR_GBP': 0.85,
            'EUR_USD': 1.08,
            'USD_GBP': 0.79,
            'USD_EUR': 0.93
        }
    
    if from_currency == to_currency:
        return amount
    
    rate_key = f"{from_currency}_{to_currency}"
    rate = exchange_rates.get(rate_key, 1.0)
    
    return round(amount * rate, 2)

def calculate_commission(
    net_amount: float,
    commission_rate: float = 0.0,
    commission_amount: float = 0.0
) -> float:
    """Calculate commission value"""
    
    if commission_rate > 0:
        commission = net_amount * (commission_rate / 100)
    else:
        commission = commission_amount
    
    return round(commission, 2)

def calculate_markup(cost: float, markup_percent: float) -> Dict[str, float]:
    """Calculate selling price with markup"""
    
    markup_amount = cost * (markup_percent / 100)
    selling_price = cost + markup_amount
    
    return {
        'markup_amount': round(markup_amount, 2),
        'selling_price': round(selling_price, 2),
        'margin_percent': round((markup_amount / selling_price) * 100, 2) if selling_price > 0 else 0
    }

def calculate_weighted_average(values: List[float], weights: List[float]) -> float:
    """Calculate weighted average"""
    
    if len(values) != len(weights) or not values:
        return 0.0
    
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    
    return round(weighted_sum / total_weight, 2) if total_weight > 0 else 0.0