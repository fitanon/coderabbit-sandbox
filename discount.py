from decimal import Decimal


def calculate_discount(price, is_member):
    # apply member discount
    if is_member:
        discount_factor = Decimal("0.90") if isinstance(price, Decimal) else 0.90
        return price * discount_factor
    return price


def total(prices):
    running_total = Decimal("0")
    for price in prices:
        running_total += price
    return running_total
