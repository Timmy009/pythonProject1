def concatenation(list1, list2):
    list3 = []
    for element in range (len(list2)):
        list3 += list2[element] +  str(list1[element])
    return list3




list1 = [1, 2, 3, 4, 5]

list2 = ["a", "b", "c", "d"]

print(concatenation(list1, list2))


def concatenation_two(list1, list2):
    list3 = []
    for element in range (len(list2)):
        list3 += list2[element] 
        list3 += (list1[element])
    return list3




list1 = [1, 2, 3, 4, 5]

list2 = ["a", "b", "c", "d"]

print(concatenation(list1, list2))