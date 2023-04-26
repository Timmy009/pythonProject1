number1 = float(input("Enter the first number: "))

number2 = float(input("Enter the second number: "))

number3 = float(input("Enter the third number: "))

num = number1, number2, number3
print(sorted(num))

if number1 <= number2 <= number3:
    arranged = number1, number2, number3
elif number1 <= number3 <= number2:
    arranged = number1, number3, number2
elif number2 <= number1 <= number3:
    arranged = number2, number1, number3
elif number2 <= number3 <= number1:
    arranged = number2, number3, number1
elif number3 <= number2 <= number1:
    arranged = number3, number2, number1
else :
    arranged = number3, number1, number2

print(f"The arranged number is {arranged}")
