score = float(input("What is your score: "))

if score >= 80:
    print("A")
elif 65 <= score <= 80:
    print("B")
elif score >= 60 and score <= 65:
    print("C")
elif score >= 40 and score <= 50:
    print("D")
elif score <= 39:
    print("B")

# result = "You fail this course" if score >= 40 else "you passed, congratulations"


