age = int(input("Enter your age: "))

maximum_heart_rate = 220 - age

lower_target_rate = 0.50 * maximum_heart_rate

higher_target_rate = 0.85 * maximum_heart_rate

print(f"The maximum heart rate is {maximum_heart_rate}")

print(f"The lower and higher target heart rate is {lower_target_rate} and {higher_target_rate} respectively")