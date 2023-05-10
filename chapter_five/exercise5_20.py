tables = [count_one * count_two for count_one in range(1, 11) for count_two in range (1, 11)]


for count in range (1, 11):
    for count_two in range (1, 11):
        multiple = count * count_two
        print(multiple, end=" ")
    print()


