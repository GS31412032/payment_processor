import sqlite3
import os

DB_PATH = 'payment_processor.db'
SQL_DIR = 'database'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def read_sql(filename):
    with open(os.path.join(SQL_DIR, filename), 'r') as f:
        return f.read()

def initialise_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(read_sql('schema.sql'))
    conn.commit()
    conn.close()

def insert_account(name, account_number, sort_code, balance):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(read_sql('insert_account.sql'), (name, account_number, sort_code, balance))
    conn.commit()
    conn.close()

def insert_transaction(sender_account_number, receiver_account_number, amount, payment_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(read_sql('insert_transaction.sql'), (sender_account_number, receiver_account_number, amount, payment_type))
    conn.commit()
    conn.close()

def update_balance(balance, account_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(read_sql('update_balance.sql'), (balance, account_number))
    conn.commit()
    conn.close()

def get_account(account_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(read_sql('get_account.sql'), (account_number,))
    account = cursor.fetchone()
    conn.close()
    return account