import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0



count = 1
while count <= 10000:
    number = random.randint(1, 6)
    if number == 1:
        one +=1
    elif number == 2:
        two +=1
    elif number == 3:
        three +=1
    elif number == 4:
        four +=1
    elif number ==5:
        five +=1
    elif number == 6:
        six +=1
    count +=1

print("Number of times one occur is ", one)
print("Number of times two occur is ", two)
print("Number of times three occur is ", three)
print("Number of times four occur is ", four)
print("Number of times five occur is ", five)
print("Number of times six occur is ", six)