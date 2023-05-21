def unique_numbers(number):
    num_list = number
    sum_list = 0
    for nam in num_list:
        sum_list += nam
    uniq = set(number)
    sum_uniq = 0
    for num in uniq:
        sum_uniq += num
    difference = sum_uniq - sum_list
    if difference % 2 == 0:
        return number
    if difference % 2 != 0:
        return uniq


def unique_numbers_two(number):
    sum_list = sum(number)
    uniq = set(number)
    sum_uniq = sum(uniq)
    if sum_list - sum_uniq % 2 == 0:
        return number
    else:
        return uniq


number = [2, 2, 3, 2, 4, 7, 7, 3]
print(unique_numbers(number))
print(unique_numbers_two(number))
