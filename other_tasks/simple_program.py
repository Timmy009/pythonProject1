def div(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzBuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return ""


for i in range(1, 101):
    print(i, div(i))
