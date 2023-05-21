from Account import Account
from decimal import Decimal


account1 = Account("Timi", Decimal(100))

if __name__ == '__main__':
    print(account1.name)
    account1.balance = 900
    print(account1.balance)
    Account.bonus = 800
    print(Account.bonus)