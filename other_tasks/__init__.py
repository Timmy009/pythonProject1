x = 4

def set_x ():
    global x
    print(id(x))

print(id(x))

print(set_x())