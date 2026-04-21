
CREATE TABLE IF NOT EXISTS accounts (
    account_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sort_code TEXT NOT NULL,
    balance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_account_number INTEGER NOT NULL,
    receiver_account_number INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_type TEXT NOT NULL,
    FOREIGN KEY (sender_account_number) REFERENCES accounts(account_number),
    FOREIGN KEY (receiver_account_number) REFERENCES accounts(account_number)
);