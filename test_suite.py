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

@pytest.fixture
def test_account():
    return Account('John Penny', 31412032, '40-47-84', 2500)

def test_account_deposit(test_account):
    # Test Deposit
    inital_balance = test_account.balance
    test_account.deposit(1000)
    assert test_account.balance > inital_balance

def test_account_withdraw(test_account):
    initial_balance = test_account.balance
    test_account.withdraw(500)
    assert test_account.balance == initial_balance - 500

def test_account_overdraft(test_account, capsys):
    test_account.withdraw(10000)
    captured = capsys.readouterr()
    assert 'Overdraft' in captured.out

def test_transaction_log(test_account):
    test_account.deposit(500)
    transactions = test_account.transactions
    assert len(transactions) > 0
    assert transactions[0]['transaction_type'] == 'deposit'
    assert transactions[0]['transaction_amount'] == 500

    


    