import random

frequency_one = 0
frequency_two = 0
frequency_three = 0
frequency_four = 0
frequency_five = 0
frequency_six = 0

for num in range(6000000):
    number = random.randrange(1, 7)

    if number == 1:
        frequency_one += 1
    elif number == 2:
        frequency_two += 1
    elif number == 3:
        frequency_three += 1
    elif number == 4:
        frequency_four += 1
    elif number == 5:
        frequency_five += 1
    elif number == 6:
        frequency_six += 1

print(frequency_one)
print(frequency_two)
print(frequency_three)
print(frequency_four)
print(frequency_five)
print(frequency_six)
