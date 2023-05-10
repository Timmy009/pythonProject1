def is_pallindrome(name):
    name = list(name.lower().rstrip())

    name_list = []
    for char in name:
        name_list.append(char)

    reversed_name = []

    count = 0
    while len(name_list) > 0:
        reversed_name += name_list.pop()
    count += 1
    if name_list == reversed_name:
        print("Yes")
    return name == reversed_name


name = input("Enter a name")
print(is_pallindrome(name))
