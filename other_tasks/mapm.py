

# list2 = [list2[a] **2 for a in range (len(list2))]







# def sqyar(number):
#     return number ** 2

list2 = [1, 2, 3, 4, 5, 8]
# ans = list(map(sqyar, list2))

# print(ans)
# print(sqyar(2))

print(list(map(lambda x: x **2, list2)))