set1 = {98, 56, 434, 1, 1, 1, 2, 2, 3, 4, 1}
set2 = {1, 3, 56, 65, 43, 5, 6}

print(set1)
if 98 in set1:
    print("Tim")

print(set1 & set2)
print(set1.union(set2))
print(set1|set2)
print(set1&set2)


students = [
    {"name": "Timi", "age": 45, "no_of_children": 6},
    {"name": "Torin", "age": 98, "no_of_children": 98},
]

print(students[0]["age"])