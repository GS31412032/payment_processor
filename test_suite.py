# A test suite to ensure test driven development is followed
import pytest
import random
from classes.accounts import Account
from classes.payment_methods import PaymentMethod, CardPayment, BankTransfer
from classes.processor import Processor

# ACCOUNT CLASS TESTING
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


# PAYMENT METHOD CLASS TESTING
def test_paymentmethod_class():
    random_amount = random.randint(0,100_000)
    method = PaymentMethod(random_amount)
    assert method.amount == random_amount

def test_cardmethod_class():
    random_amount = random.randint(0,100_000)
    card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    month = random.randint(1, 12)
    year = random.randint(25, 30)
    expiry = f"{month:02d}/{year}"
    cvv = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    payment = CardPayment(random_amount, card_number, expiry, cvv, pin)
    assert payment.amount == random_amount
    assert payment.card_number == card_number
    assert payment.expiry_date == expiry
    assert payment.cvv == cvv
    assert payment.pin == pin
    assert payment.validate() == True

    false_payment = CardPayment(100, '123', '05/28', '99', '111')
    assert false_payment.validate() == False

def test_BankTransfer_class():
    random_amount = random.randint(0,100_000)
    sort_code = '-'.join([f"{random.randint(0, 99):02d}" for _ in range(3)])
    account_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    reference = 'Hello World'

    payment = BankTransfer(random_amount, sort_code, account_number, reference)
    assert payment.amount == random_amount
    assert payment.sort_code == sort_code
    assert payment.account_number == account_number
    assert payment.reference == reference
    assert payment.validate() == True

    false_payment = BankTransfer('123', '05/28', '99', '111')
    assert false_payment.validate() == False



# PROCCESSOR CLASS TESTING
def test_proccesor_class():
    sender = Account('John Penny', 31412032, '40-47-84', 2500)
    reciever = Account('Jane Smith', 12345678, '20-30-40', 1000)
    method = BankTransfer(500, '40-47-84', '31412032', 'Hello World')

    processor = Processor()
    processor.process_payment(sender, reciever, method)
    
    assert sender.balance == 2000
    assert reciever.balance == 1500

    method = BankTransfer(10000, '40-47-84', '31412032', 'Hello World')
    processor.process_payment(sender, reciever, method)
    assert sender.balance == 2000
    assert reciever.balance == 1500

    invalid_method = BankTransfer(500, 'bad-sort', '31412032', 'Hello World')
    processor.process_payment(sender, reciever, invalid_method)
    assert sender.balance == 2000
    assert reciever.balance == 1500

    


    