for col in range(0, 4):
    if col == 0:
        print(" ", end=" ")
    print(col, end=" ")

for row in range(4):
    print(row, end=" ")
    for column in range(4):
        if row == 1 and column == 1:
            print(16, end=" ")
        else:
            print(0, end=" ")
    print()
