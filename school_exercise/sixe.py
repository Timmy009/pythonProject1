from sys import getsizeof

double = [ a ** 2 for a in range (1000000)]
doubles = (a ** 2 for a in range (1000000))

print(getsizeof(double))
print(getsizeof(doubles))