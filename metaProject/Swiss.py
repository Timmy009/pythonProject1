from metaProject.Bank import Bank


class Swiss(Bank):
    def __init__(self):
        bal = 1000

    def basic_info(self) ->str:
        print("This is the Swiss Bank")
        return f"Swiss bank : {self.__bal} "

    def withdraw(amount):
        return bal - amount





