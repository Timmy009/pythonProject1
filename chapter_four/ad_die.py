import random


def dies():
    die_one = random.randrange(1, 7)
    die_two = random.randrange(1, 7)
    return die_one, die_two


def display_dies(dies):
    die_one, die_two = dies
    print(f"The sum of {die_one} + {die_two} is {die_one + die_two}")


roll_die = dies()
display_dies(roll_die)
print(roll_die)
if sum(dies()) in (7, 11):
    print("You win")
elif sum(dies()) in (2, 3, 12):
    print("You lose")
else:
    roll_die = dies()
    display_dies(roll_die)
    while sum(dies()) != (4, 5, 6, 8, 9, 10):
        roll_die = dies()
        display_dies(roll_die)
        print(roll_die)
        if roll_die == 7:
            print("You lose")
            break
    else:
        print("You won")
