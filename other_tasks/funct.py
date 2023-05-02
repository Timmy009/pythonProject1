def mult(num, num2):
    return num * num2


print(mult(num2=3, num=2))


def add(*args):
    product = 0
    for nu in args:
        product = product + nu
    return product

n = [2, 4, 5, 6, 7]



print(add(*n))

x = 3

def scopV_va ():
    global x
    x = 6
    print(x)

scopV_va()
print(x)
