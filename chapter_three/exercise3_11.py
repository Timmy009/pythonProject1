number_of_does = 0
total_baby_rabbits = 0
while number_of_does != -1:
    number_of_does = int(input("Enter the number of does in the rabbit colony (-1 to end): "))
    if number_of_does == -1:
        break
    baby_rabbits = int(input("Number of baby rabbits born in the past month: "))
    total_baby_rabbits = total_baby_rabbits + baby_rabbits
    print(f"On average {baby_rabbits / number_of_does} baby rabbits were born for each doe")

print(f"Total number of baby rabbits for each doe so far: {total_baby_rabbits}")