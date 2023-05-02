doubles = {}

# for a in range(1, 10):
#     doubles[a] = a ** 2


doubles = {a: a**2 for a in range (1, 10)}
print(doubles)


double2 = (a**2 for a in range (1, 10))
print(double2)