from classes.accounts import Account
from classes.payment_methods import PaymentMethod, CardPayment, BankTransfer

class Processor():
    def __init__(self):
        self.transaction_log = []

    def process_payment(self, sender, receiver, payment_method):
        self.sender = Account(sender)
        self.receiver = Account(receiver)





