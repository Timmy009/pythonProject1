cart = [["Timmy", 500, 10, 5000, "08069547786"],
        ["Feranmi", 400, 10, 4000, "09024943627"],
        ["Hassan", 680, 10, 6800,  "08148517717"],
        ["Eunice", 790, 10, 7900,  "08066409589"],
        ["Esther", 900, 10, 9000, "07067039728"]]

cart[0][1] = 7800
print(cart)
cart[1][0] = "David"
print(cart)
# cart.extend(["Tayo", 400, 10, 4000, "0903747884"])
cart.append(["taiwo", 300, 10, 3000, "09038374747"])
print(cart)
cart.pop(0)
print(cart)


even_number1 = [i for i in range(21) if i % 2 == 0]
print(even_number1)


even_number = []
for num in range (0, 51):
        if num % 2 == 0:
                even_number.append(num)

even_number2 = []
print(even_number)