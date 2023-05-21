def zero_re(lst):
    lst[0] = 0
    lst[-1] = 0
    return lst


lst = [2, 5, 4, 6, 7, 8]
print(zero_re(lst))