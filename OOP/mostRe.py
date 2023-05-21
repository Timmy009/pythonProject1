import statistics


def most_occur(lst):
    return statistics.mode(lst)

lst = [2, 5, 7, 5, 4, 3]
print(most_occur(lst))
