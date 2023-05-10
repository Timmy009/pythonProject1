responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3,
1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range (1, 6):
    print(f"{i} appears {responses.count(i)}")

color_names = ['red', 'orange', 'yellow', 'green', 'blue']

color_names.reverse()
print(color_names)

ti = color_names.copy()

print(ti)


# even_number = [number + 2 for number in range (0, 51, 2)]
#
# print(even_number)
#
# even_number2 = list(range(0, 51, 2))
#
# print(even_number2)

even = [number for number in range (0, 51, 2) if 1 < 10]

print(even)

name = ["taye", "kenny"]

name2 = [item.upper() for item in name]

print(name2)