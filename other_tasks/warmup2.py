def string_tr(list3 : list):
    for row in range(len(list3)):
        for col in range(len(list3)):
            if list3[row] == list3[col]:
                return f"There is a duplicate, which is {list3[row]}"
            else:
                return "There is no duplicate"


list3 = ["su", "ma", "tm", "su"]
print(string_tr(list3))


def string_tr2(list3):
    list6 = set(list3)
    if len(list3) == len(list6):
        return f"There is no duplicate"
    else:
        return f"There is a duplicate"


def duplicate2 (lzt):
    for item in lzt:
        if lzt.count(item) > 1:
            return f"The item {item} occured more than once"
        else:
            return f"There is no duplicate"


print(string_tr2(list3))
print(duplicate2(list3))