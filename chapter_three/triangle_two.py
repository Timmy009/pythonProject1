for number in range (12, 1, -1):
    for number_three in range (number, 12, 1):
        print(' ', end='')
    for number_two in range (1, number):
        print('*', end='')
    print()