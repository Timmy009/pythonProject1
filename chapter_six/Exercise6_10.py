def comopare(set1, set2):
    if len(set1) > len(set2):
        return "Set1 is greater than set2"
    else:
        return "Set2 is greater than set2"


def nat_comopare(set1, set2):
    if set1 == set2:
        return "Set1 and set2 are equal"
    else:
        return "set1 and set2 are not equal"


def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    s_difference = set1 ^ set2
    return union, intersection, difference, s_difference


set1 = {"red", "blue", "green", "yellow"}
set2 = {"blue", "green", "orange", "purple"}
print(comopare(set1, set2))
print(nat_comopare(set1, set2))
print(set_operations(set1, set2))
