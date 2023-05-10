list1 = [1, 2, 3, 4, 5]

print(*list1)





while True:
    print("Please chhose between the below options")
    print("1.\tLearn python")
    print("2.\tLearn java")
    print("3.\tGo swimming")
    print("4.\tHave dinner")
    print("5.\tGo to bed")
    print("0\tExit")
    choice = input()

    if choice == "0":
        break
    elif choice in "012345":
        print(f"You chose{choice}")
    else:
        continue