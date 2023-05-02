print("Timi".count("i"))



# list unpacking
my_list = [1, 2, 3, 4, 5]
# x, y, a, b, c = my_list


letters = list ("Hello c16")
print(letters)

for index, letter in enumerate (letters):
    print(index, letter)
x, *others, y = my_list
print(y)
print(x, others, y)
# x , y, *others = my_list

print(others)
print(y)
name = my_list[::-1]

print(name)

students = [["sultan", 35, 200, 90.9], ["mariam", 32, 200, 95]]

print(students[1][2])

print(students[0])

ones = [1] * 100
print(ones)

list2 = students + my_list

print(list2)




letters1 = ["a", "b", "c", "d"]

letters1.append("ef")

letters1.append("f")

letters1.remove("a")
letters1.insert(0, "z")


del letters1[0:2]
print(letters1)