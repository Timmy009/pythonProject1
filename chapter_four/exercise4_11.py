import random


def get_random_number ():
    return random.randint(1, 10)

def correct_product(number_one, number_two):
    return number_one * number_two

def get_player_product():
    number_one = get_random_number()
    number_two = get_random_number()
    product = input(f"What is the product of {number_one} * {number_two}")
    return product

def get_computer_product(number_one, number_two):
    pruduct = number_one * number_two
    if random.random() < 0.1:
        pruduct = get_random_number() + 8
    return pruduct

def play_game():

    play_again = "yes"

    user_count = 0
    computer_count = 0
    while play_again.startswith("y"):
        number_one = get_random_number()
        number_two = get_random_number()
        get_player_product()
        get_computer_product(number_one, number_two)
        if get_player_product() == number_one * number_two:
            print("User Correct!")
            user_count +=1
            if  get_computer_product(number_one, number_two) == number_one * number_two:
                print("Computer correct!")
                computer_count +=1

        else:
            print(f"Your score is {user_count}")
            print(f"The computer score is {computer_count}")
            if user_count > computer_count:
                print("User won")
            else:
                print("Computer won")
            break
    play_again = input("Do you want to play again?: y/n")






play_game()