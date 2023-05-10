import random

ids = []

count = 1
while count <= 8000:
    choice = random.choice(["a", "b", "c", "d", "e", "f"])
    number_one = random.randint(1, 4)
    number_two = random.randint(1, 4)
    id = choice + str(number_one) + str(number_two)
    ids.append(id)
    count+=1


unique_value = sorted (set(ids), reverse=True)

print(unique_value)