def discount(price):
    dis = 0.1 * price
    return f"You have been given 10% discount which is {dis}. Your new price is {price - dis}"


price = int(input("Enter price: "))

print(discount(price))
