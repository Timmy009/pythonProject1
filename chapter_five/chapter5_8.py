import random


def insertion(number):
    for num in range(len(number)):
        for num2 in range(num + 1, len(number)):
            if number[num] > number[num2]:
                number[num], number[num2] = number[num2], number[num]
    return number


number = random.sample(range(0, 100), 10)

print(sorted, insertion(number))
