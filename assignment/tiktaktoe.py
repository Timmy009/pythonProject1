

gameInput = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
for i in gameInput:
    print("___________________ ", )
    for j in i:
        print("| ", j, "|", end="")
    print()


# player1 = int(input("Player 1 play"))
# player2 = int(input("Player 2 play"))

def display(gameInput):
    print("GAME ON")
    for i in gameInput:
        print("___________________ ", )
        for j in i:
            print("| ", j, "|", end="")
        print()
def play(gameInput):
    player1 = (input("Player 1 play"))
    player2 = input("Player 2 play")
    if player1 == 1:
        if gameInput[0][0] == "O" or gameInput[0][0] == "X":
            print("This position has been played before. Replay")
            play(gameInput)
        else:
            gameInput[0][0] = "O"
            display(gameInput)
    if (player2 ==1):
        if gameInput[0][0] == "O" or gameInput[0][0] == "X":
            print("This position has been played before. Replay")
            play(gameInput)
        else :
              gameInput[0][0] = "O"
              display(gameInput)
    if (player1 == 2):
        if gameInput[0][1] == "O" or gameInput[0][1] == "X":
            print("This position has been played before. Replay")
            play(gameInput)
        else:
            gameInput[0][1] = "O"
            display(gameInput)
    if (player2 == 2):
        if gameInput[0][1] == "O" or gameInput[0][1] == "X":
            print("This position has been played before. Replay")
            play(gameInput)
        else:
            gameInput[0][1] = "O"
            display(gameInput)


        if gameInput[0][2] == "O" or gameInput[0][2] == "X":
            print("This position has been played before. Replay")
            play(gameInput)
        else:
            gameInput[0][2] = "O"
        display()
    if (player1 == 4 or player2==4):
        if gameInput[1][0] == "O" or gameInput[1][0] == "X":
            print("This position has been played before. Replay")
            play(player1, player2)
        else:
            gameInput[1][0] = "O"
        display()
    if (player1 == 5 or player2 ==5):
        if gameInput[1][1] == "O" or gameInput[1][1] == "X":
            print("This position has been played before. Replay")
            play(player1, player2)
        else:
            gameInput[1][1] = "O"
        display()
    if (player1 == 6 or player2 ==6):
        if gameInput[1][2] == "O" or gameInput[1][2] == "X":
            print("This position has been played before. Replay")
            play(player1, player2)
        else:
            gameInput[1][2] = "O"
        display()
    if (player1 == 7 or player2 ==7):
        if gameInput[2][0] == "O" or gameInput[2][0] == "X":
            print("This position has been played before. Replay")
            play(player1, player2)
        else:
            gameInput[2][0] = "O"
        display()
    if (player1 == 8 or player2 ==8):
        if gameInput[2][1] == "O" or gameInput[2][1] == "X":
            print("This position has been played before. Replay")
            play(player1, player2)
        else:
            gameInput[2][1] = "O"
        display()
    if (player1 == 9 or player2 ==9):
        if gameInput[2][2] == "O" or gameInput[2][2] == "X":
            print("This position has been played before. Replay")

        else:
            gameInput[2][2] = "O"
        display()



play(gameInput)