number = list(range(1, 21))

print(number)


number[4:11] = [0] * len(number[5:10])

print(number)

od = number[::2]

print(od)

odd_num = list(range(1, 21, 2))

print(odd_num)

odd_number = [odd for odd in number if odd % 2 != 0]

print(odd_number)

for item in range(4, 10):
    number[item] = 0
print(number)

print(number[:7])
# number.clear()
number[:] = []

print(number)
print(number)

