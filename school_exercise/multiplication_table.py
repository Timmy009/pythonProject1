print("\t\t\t\tMULTIPLICATION TABLE")


def multiple(times: int):
    for num in range(1, 13):
        for num2 in range(1, times +1 ):
            print(end=" " f"H|H{num2 : >3}  * {num: >3}  = {num * num2: >3}  ")
        print()

multiple(20)