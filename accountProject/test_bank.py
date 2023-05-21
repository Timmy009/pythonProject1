from accountProject.bank import bank
import pytest

def test_for_register_for_bank_account_with():
    ban = bank()
    ban.register("timmy", "08069547786", "1234")
    assert ban.number_of_accounts() == 1

def test_to_deposit():
    ban = bank()
    ban.register("timmy", "08069547786", "1234")
    account_number = ban.request_accountnumber("timmy")
    print(account_number)
    ban.deposit(account_number, 5000)
    assert ban.check_account_balance(account_number) == 5000


def test_to_deposit_negative_amount():
    ban = bank()
    ban.register("timmy", "08069547786", "1234")
    account_number = ban.request_accountnumber("timmy")
    print(account_number)
    ban.deposit(account_number, -5000)
    assert ban.check_account_balance(account_number) == 0

def test_to_withdraw():
    ban = bank()
    ban.register("timmy", "08069547786", "1234")
    account_number = ban.request_accountnumber("timmy")
    print(account_number)
    ban.deposit(account_number, 15000)
    ban.withdrawal_in_accounts(account_number, 5000, "1234")
    assert ban.check_account_balance(account_number) == 10000
