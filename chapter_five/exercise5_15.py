from operator import itemgetter

invoices = [('83', 'Electric sander', 7, 57.98),
            ('24', 'Power saw', 18, 99.99),
            ('7', 'Sledge hammer', 11, 21.5),
            ('77', 'Hammer', 76, 11.99),
            ('39', 'Jig saw', 3, 79.50)]

sorted_by_description = sorted(invoices, key=itemgetter(1))

for invoice in sorted_by_description:
    print(invoice)
print()
sorted_by_price = sorted(invoices, key=itemgetter(3))

for invoice in sorted_by_price:
    print(invoice)

print()
map_item_des = sorted([(invoice[1], invoice[2]) for invoice in invoices], key=itemgetter(1))

for item in map_item_des:
    print(item)

map_value = sorted([(invoice[1], invoice[2] * invoice[3]) for invoice in invoices], key=itemgetter(1))

print()

for inv in map_value:
    print(inv)

print()

filtered_result = filter(lambda item: 200 <= item <= 500, map_value)

for fil in filtered_result:
    print(fil)

print()
the_sum = sum([invoice[2] * invoice[3] for invoice in invoices])

print(the_sum)
