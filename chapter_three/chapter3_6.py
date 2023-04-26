first_question = input("What is your problem: ")

second_question = input("Have you had this problem before? (yes or no): ")

if second_question.lower() == "yes":
    print("Well, you have it again")
else:
    print("Well, you have it now")
