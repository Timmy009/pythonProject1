binary_number = (input("Enter a binary digit: "))
num = 0
count = 1
count_two =1
binary_digit = int (binary_number)
while count <= len(binary_number) :
    digit = binary_digit % 10
    num = num +  digit * count_two
    count_two = count_two *2
    binary_digit = binary_digit // 10
    count += 1

print(num)