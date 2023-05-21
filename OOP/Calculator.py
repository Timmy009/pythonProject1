def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def substratction(a, b):
    return a + b


def division(a, b):
    return a / b


def calculator(a: int, b: int, operator: str):
    if operator == "+":
        return addition(a, b)
    if operator == "*":
        return multiplication(a, b)
    if operator == "-":
        return substratction(a, b)
    if operator == "/":
        return division(a, b)


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
operator = (input('Enter the operator: '))
print(calculator(a, b, operator))
