def get_largest_element(list2):
    largest_element = list2[0]
    for element in list2:
        if element > largest_element:
            largest_element = element
    return largest_element


list2 = [1, 2, 3, 9, 6, 5]
print(get_largest_element(list2))
