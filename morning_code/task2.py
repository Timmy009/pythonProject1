list2 = ["male", "female", "Female", "male", "Male", "male", "female"]


def turple_gen(list2):
    male_count = 0
    female_count = 0
    for index, name in enumerate(list2):
        if list2[index].lower() == "male":
            male_count += 1
        else:
            female_count += 1

    tur = [(list2[0], male_count), (list2[1], female_count)]
    return tur


print(turple_gen(list2))
