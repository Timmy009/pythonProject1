

num_of_days = 7
total = 0

minimum_value = float('inf')
maximum_value = float('-inf')
for number in range(1, num_of_days + 1):
    user_input = int(input("Enter the number of reported infections: "))
    total = total + user_input
    if user_input < minimum_value:
        minimum_value = user_input
    if user_input > maximum_value:
        maximum_value = user_input

average = total / num_of_days
print(f"The total infections is {total}")
print(f"The average infections is {average}")
print(f"The minimum value is {minimum_value}")
print(f"The maximum value is {maximum_value}")