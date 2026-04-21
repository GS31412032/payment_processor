-- Insert new account into the accounts table
INSERT INTO accounts (name, account_number, sort_code, balance)
VALUES (?, ?, ?, ?);

-- Insert new transaction into transactions table
INSERT INTO transactions (sender_account_number, receiver_account_number, amount, payment_type) 
VALUES (?, ?, ?, ?);

-- Update account balance after a transaction
UPDATE accounts SET balance = ? WHERE account_number = ?;

-- Retrieve account details by account number
SELECT * FROM accounts WHERE account_number = ?;