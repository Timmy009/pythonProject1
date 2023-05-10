def calculate_sum_for_loop(list2):
    the_sum = 0
    for element in list2:
        the_sum += element
    return the_sum





def calculate_sum_with_while_loop(list2):
    the_sum = 0
    count = 0
    while count < len(list2):
        the_sum+=list2[count]
        count+=1
    return the_sum



list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(calculate_sum_with_while_loop(list2))

print(calculate_sum_for_loop(list2))



list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(calculate_sum_for_loop(list2))
