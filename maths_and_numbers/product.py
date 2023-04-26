def multiple (*lst):
    product = 1
    for num in lst:
        product *= num
    return product


print(multiple(4, 2))