from classes.accounts import Account
from classes.payment_methods import PaymentMethod, CardPayment, BankTransfer

class Processor():
    def __init__(self):
        self.transaction_log = []

    def process_payment(self, sender, receiver, payment_method):

        # Validate Payment Method
        if not payment_method.validate():
            print('Invalid payment details')
            return

        # Validate Transaction
        if sender.balance >= payment_method.amount:
            sender.withdraw(payment_method.amount, receiver)
            receiver.deposit(payment_method.amount, sender)
            self.transaction_log.append({
                'sender': sender.name,
                'receiver': receiver.name,
                'amount': payment_method.amount,
                'payment_type': type(payment_method).__name__
            })
            print(f'Transaction Complete')

        else:
            print(f'Insufficient Funds')






