lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]


def sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


print(sort(lst))
