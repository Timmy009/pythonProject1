import random

actors = ['Sean Bean', 'Mark Addy', 'Nikolaj Coster-Waldau', 'Michelle Fairley', 'Lena Headey']
characters = ['Ned Stark', 'Robert Baratheon', 'Jaime Lannister', 'Catelyn Stark', 'Cersei Lannister']
random.shuffle(characters)

correct_answer = 0
for character in characters:
    print(f"Who played {character}: ")
    actor =  answer = input()

    if actor in actors and characters[actors.index(actor)] == character:
        print("Correct")
        correct_answer +=1
    else:
        print("Incorrect")

print(f"You got {correct_answer} out of 5 correct")
