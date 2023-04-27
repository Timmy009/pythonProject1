principal = float(input("Enter the principal amount you want to invest: "))
year = int(input("Enter the number of years: "))
rate = 0.05

def calculate_interest(principal: float, year: int):
    count = 1
    while count <= year:
        interest = rate * principal
        future_value = principal + interest
        principal = future_value
        print(f"Year {count} investment yields {interest: .2f}, your principal is now {future_value: .2f}")
        count += 1
calculate_interest(principal, year)
