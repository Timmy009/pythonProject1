import random

play_again = "yes"

user_count = 0

while play_again.startswith("y"):
    num1 = random.randrange(1, 10)

    num2 = random.randrange(1, 10)

    correct_answer = num1 * num2

    user_response = int(input(f"What is {num1} times {num2} "))

    if user_response == correct_answer:
        print("Correct!")
        user_count +=1
    else:
        print("Incorrect")
        break
    play_again = input("Do you want to play again?: y/n")


print(f"The number of correct trials are {user_count}")