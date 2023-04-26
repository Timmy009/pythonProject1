count = 0
while count < 10:
    print("year name", end = " ")
    count+=1
print("\n", count)

for letter in "Victoria":
    print(letter)

for letter in "12345":
    print(letter)

for count in range (4, 10):
    print(count)

for count in range (0, 11, 2):
    print(count)


for count in range (1, 11):
    for counter in range (1, count):
        print(" ", end = "")
    for countTwo in range (count, 0):
        print("*")
    print()

for i in range (7):
    print("step")
    for i in range (3):
        print("clap")
    print()

