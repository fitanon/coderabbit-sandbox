def calculate_discount(price, is_member):
    # apply member discount
    if is_member == True:
        return price * 0.90
    return price


def total(items):
    sum = 0
    for i in items:
        sum = sum + items[i]
    return sum
