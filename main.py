from classes.accounts import Account
from classes.processor import Processor
from classes.payment_methods import PaymentMethod, CardPayment, BankTransfer
from database.db import reset_db
reset_db()

# Initiate Bank Accounts
# card transfers
jp_account = Account('John Penny', 31412032, '40-47-84', 2500)
js_account = Account('Jane Smith', 12345678, '20-30-40', 1000)
method = CardPayment(200, '1234567890123456', '05/28', '123', '1234')
processor = Processor()
processor.process_payment(jp_account, js_account, method)
jp_account.transaction_history()
js_account.transaction_history()

# bank transfers
hm_account = Account('Hessel Morgan', 36445698, '26-45-51', 100000)
os_account = Account('Olaf Shanks', 87924100, '71-84-19', 1_000_000)
method = BankTransfer(30_000, '26-45-51', '36445698', 'Equity Investment')
processor = Processor()
processor.process_payment(hm_account, os_account, method)
hm_account.transaction_history()
os_account.transaction_history()

# Insufficent Funds Payment
method = BankTransfer(100_000, '40-47-84', '31412032', 'Private Equity Transfer')
processor = Processor()
processor.process_payment(jp_account, os_account, method)
jp_account.transaction_history()
os_account.transaction_history()

