# A test suite to ensure test driven development is followed
import pytest
from classes.accounts import Account

@pytest.mark.parametrize("name, account_number, sort_code, balance", [
    ('John Penny', 31412032, '40-47-84', 2500),
    ('Jane Smith', 12345678, '20-30-40', 1000),
])
def test_account_class(name, account_number, sort_code, balance):
    account = Account(name, account_number, sort_code, balance)
    assert account.name == name
    assert account.account_number == account_number
    assert account.sort_code == sort_code
    assert account.balance == balance

def test_account_functions():
    print('hello')

    