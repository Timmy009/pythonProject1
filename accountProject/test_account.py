import pytest
from accountProject.Account import Account




def test_deposit():
    ac = Account("Timmy", "94389489438943", "1234")
    ac.deposit(3000)
    assert ac.check_balance() == 3000


def test_for_negative_deposit():
    ac = Account("Timmy", "94389489438943", "1234")
    ac.deposit(-3000)
    assert ac.check_balance() == 0


def test_for_withdrawal():
    ac = Account("Timmy", "94389489438943", "1234")
    ac.deposit(5000)
    ac.withdrawal(3000, "1234")
    assert ac.check_balance() == 2000

def test_for_negative_withdrawal():
    ac = Account("Timmy", "94389489438943", "1234")
    ac.deposit(5000)
    ac.withdrawal(-3000, "1234")
    assert ac.check_balance() == 5000
