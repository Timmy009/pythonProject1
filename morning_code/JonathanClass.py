def arr_spread (number):
    res = []
    for n in str(number):
        for x in n.removesuffix('',):
           res.append(x)
    return res


t = [106, 25, 43, 62, 12]

print(arr_spread(t))


# def arr_spread_two (number):
#     number = list (number)
#     res = []
#     for index, n in enumerate(number):
#         for x in n:
#             res.append(x)
#     return res
#
#
# t = [10, 25, 43, 62, 12]
#
# print(arr_spread(t))