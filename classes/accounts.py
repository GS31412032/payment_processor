from database.db import insert_account, update_balance
# Define an account class to hold relevant account details.
class Account():
    def __init__(self, name, account_number, sort_code, balance):
        self.name = name
        self.account_number = account_number
        self.sort_code = sort_code
        self.balance = balance
        self.transactions = []
        insert_account(name, account_number, sort_code, balance)

    def deposit(self, deposit_amount, sender=None):
        self.balance += deposit_amount
        transaction = {
            'transaction_type': 'deposit',
            'transaction_amount': deposit_amount,
            'sender': sender
        }
        self.transactions.append(transaction)
        update_balance(self.balance, self.account_number)

    def withdraw(self, withdraw_amount, receiver=None):
        overdraft_limit = -1000
        if self.balance - withdraw_amount > overdraft_limit:
            self.balance -= withdraw_amount
            transaction = {
                'transaction_type': 'withdrawal',
                'transaction_amount': withdraw_amount,
                'receiver': receiver
            }
            self.transactions.append(transaction)
            update_balance(self.balance, self.account_number)
            return True
        else:
            print(f'Withdraw Amount would surpass Overdraft Limit: {overdraft_limit}')
            return False

    def check_balance(self):
        print(f'Your Current Balance: {self.balance}')
        return self.balance

    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
        return self.transactions