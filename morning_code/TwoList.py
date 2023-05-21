def con_two(num1, num2):
    res = []
    for item in num1:
        for item2 in num2:
            if item == item2:
                res.append(item)
    return tuple(res)


def common_element(a, b):
    return tuple([i for i in a if i in b])

num1 = [1, 2, 3, 4, 5]
num2 = [4, 0, 7, 3, 2]

print(con_two(num1, num2))

