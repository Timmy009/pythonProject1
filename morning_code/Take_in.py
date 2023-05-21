def ret(a, b):
    if isinstance(a,float) or isinstance(b, float) :
        return a + b
    else:
        raise TypeError


a = 6
b = 9.4
print(ret(a, b))
