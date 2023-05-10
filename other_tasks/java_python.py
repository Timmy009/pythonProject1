names = []
count = 0
while count < 5:
    name = input("Enter a name: ")
    name.strip()
    if 10 >= len(name) > 0:
        names.append(name)
    count += 1

print(names)
