
class Account():

    def __init__(self, name, account_number, sort_code, balance):
        self.name = name
        self.account_number = account_number
        self.sort_code = sort_code
        self.balance = balance
        self.transactions = []
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        transaction = {
                'transaction_type': 'deposit',
                'transaction_amount': deposit_amount
            }
        self.transactions.append(transaction)

    def withdraw(self, withdraw_amount):
        overdraft_limit = -1000
        if self.balance - withdraw_amount > overdraft_limit:
            self.balance -= withdraw_amount
            transaction = {
                'transaction_type': 'withdrawl',
                'transaction_amount': withdraw_amount
            }
            self.transactions.append(transaction)
        else:
            print(f'Withdraw Amount would surpass Overdraft Limit: {overdraft_limit}')

    def check_balance(self):
        print(f'Your Current Balance: {self.balance}')
    
    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
        return self.transactions

