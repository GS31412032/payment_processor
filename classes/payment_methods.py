import re
class PaymentMethod():
    def __init__(self, amount):
        self.amount = amount


class CardPayment(PaymentMethod):
    def __init__(self, amount, card_number, expiry_date, cvv, pin):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.pin = pin
    
    def validate(self):
        return len(self.card_number) == 16 and len(self.cvv) == 3 and len(self.pin) == 4


class BankTransfer(PaymentMethod):
        def __init__(self, amount, sort_code, account_number, reference):
            super().__init__(amount)
            self.sort_code = sort_code
            self.account_number = account_number
            self.reference = reference
        
            
        def validate(self):
            return len(self.account_number) == 8 and bool(re.match(r'^\d{2}-\d{2}-\d{2}$', self.sort_code)) and type(self.reference) == str



