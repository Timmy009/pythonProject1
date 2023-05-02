def fib(first_number, second_number, third_number):
    fourth = second_number + third_number
    fifth = fourth + third_number
    six = fourth + fifth
    return fourth, fifth, six


first_number, second_number, third_number = 0, 1, 1

for fi in range(3):
    print(fib(first_number, second_number, third_number))
    first_number, second_number, third_number = fib(first_number, second_number, third_number)