list2 = list(range(1, 11))

even_integers = list(filter(lambda x: x % 2 == 0, list2))

trippled = list(map(lambda x: x * 3, even_integers))

sum_int = sum(trippled)

print(sum_int)

even_comp = [x for x in list2 if x % 2 == 0]

trippled_comp = [x * 3 for x in even_comp ]

sum_comp = sum(trippled_comp)

print(sum_comp)