from accountProject.Account import Account


class bank:

    def __init__(self):
        self.__accounts = []
        self.__bank_number = 23980978

    def register(self, name, phone_number, pin):
        new_account = Account(name, phone_number, pin)
        self.__accounts.append(new_account)
        new_account.set_account_number(self.generate_account_number())
        new_account.set_pin(pin)

    def validate_pin_for_accounts(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account.get_pin()

    def generate_account_number(self):
        return self.__bank_number + len(self.__accounts)

    def number_of_accounts(self):
        return len(self.__accounts)

    def request_accountnumber(self, accountname):
        for account in self.__accounts:
            if account.get_account_name() == accountname:
                return account.get_account_number()

    def deposit(self, account_number, amount):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.deposit(amount)

    def check_account_balance(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account.check_balance()

    def withdrawal_in_accounts(self, account_number, amount, pin):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.withdrawal(amount, pin)
            else :
                return 0
