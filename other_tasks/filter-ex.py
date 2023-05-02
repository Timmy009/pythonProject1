list1 = list(range(1, 11))


def odd_value(n):
    if n % 2 != 0:
        return n


print(list(filter(odd_value, list1)))


def odd_num(lzt):
    odd = []
    for i in lzt:
        if i % 2 != 0:
            odd.append(i)
    return odd

print(odd_num(list1))
