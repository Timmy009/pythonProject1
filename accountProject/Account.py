class Account:
    def __init__(self,  name, phone_number, pin):
        self.__balance = 0
        self.__account_number = 0
        self.__name = name
        self.__phone_number = phone_number
        self.__pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def check_balance(self):
        return self.__balance

    def withdrawal(self, amount, pin):
        if amount > 0:
            self.__balance -= amount

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

    def get_account_name(self):
        return self.__name

    def set_account_name(self, account_name):
        self.__name = account_name

    def set_pin(self, pin):
        self.__pin = pin


