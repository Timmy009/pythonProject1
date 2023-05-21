def no_ar(price, discount_rate):
    if price < 0 or discount_rate < 0:
        raise ValueError
    if isinstance(price, str) or isinstance(discount_rate, str):
        raise TypeError
    else:
        discount = discount_rate * price
        return price - discount

