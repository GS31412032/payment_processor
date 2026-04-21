from database.db import insert_transaction

class Processor():
    def __init__(self):
        self.transaction_log = []

    def process_payment(self, sender, receiver, payment_method):
        if not payment_method.validate():
            print('Invalid payment details')
            return

        if sender.withdraw(payment_method.amount, receiver.name):
            receiver.deposit(payment_method.amount, sender.name)
            self.transaction_log.append({
                'sender': sender.name,
                'receiver': receiver.name,
                'amount': payment_method.amount,
                'payment_type': type(payment_method).__name__
            })
            insert_transaction(sender.account_number, receiver.account_number, payment_method.amount, type(payment_method).__name__)
            print('Transaction Complete')
        else:
            print('Insufficient Funds')