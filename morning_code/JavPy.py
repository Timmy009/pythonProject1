def sudoku():
    num = [[], [], [], [], [], [], [], [], []]

    count = 0
    while count < 9:
        count_two = 0
        while count_two < 9:
            inpu = input("Enter number: ")
            num[count].append(inpu)
            count_two = count_two + 1
        count = count + 1
        for n in num:
            print(n)
    for index_two, n in enumerate(num):
        for index, m in enumerate(n):
            if m == m[index_two]:
                return "This is not valid"

print(sudoku())
