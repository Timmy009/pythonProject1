binary_integer = input("Input an integer containing 0 and 1: ")

count = 1
count_two = len(binary_integer) *2
digit = 0
while count <= len(binary_integer):
    digit += int(binary_integer[count - 1]) * count_two
    count += 1
    count_two //= 2

print(digit)
