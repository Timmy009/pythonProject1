user_input = int (input("Enter number: "))

first = 0
second = 1
print(first)
print(second)
for number in range(2, 10, 2):
    if user_input == first or user_input == second:
        print(f"The index of the number in the fibonacci is {number}")
    first = first + second
    second = first + second
    print(first)
    print(second)