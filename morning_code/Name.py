def gmail(name):
    if isinstance(name, int):
        raise TypeError("Invalid mail")
    name = name + "@gmail.com"
    return name


# print(gmail(5))