def pen (n):
    num1 = n * (3*n - 1) / 2

    return num1

i = 1
while i < 100:
    print(pen(100), end="")

    if i % 10 ==0:
        print()

    i = i + 1
