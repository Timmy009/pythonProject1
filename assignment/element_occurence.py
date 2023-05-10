def element_occ(number, list2):
    if number in list2:
        return f"{number} occurs"
    else:
        return f"{number} does not occur"

list2 = [1, 2, 3, 4, 5, 3]
print(element_occ(4, list2))

print(element_occ(49, list2))