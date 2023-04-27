for number in range (12, 1, -1):
    for number_four in range(12, 1, -1):
        if number_four in range (number, 12, 1):
            print(' ', end='')
        if number_four in range (1, number):
            print('*', end='')
    print()