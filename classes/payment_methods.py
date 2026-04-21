
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


class BankTransfer(PaymentMethod):
        def __init__(self, amount, sort_code, card_number, reference):
            super().__init__(amount)
            self.sort_code = sort_code
            self.card_number = card_number
            self.reference = reference


