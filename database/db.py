import sqlite3
import os

DB_PATH = 'payment_processor.db'
SQL_DIR = 'database'

conn = None

def get_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL")
    return conn

def read_sql(filename):
    with open(os.path.join(SQL_DIR, filename), 'r') as f:
        return f.read()

def reset_db():
    global conn
    if conn:
        conn.close()
        conn = None
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    initialise_db()

def initialise_db():
    c = get_connection()
    c.cursor().executescript(read_sql('schema.sql'))
    c.commit()

def insert_account(name, account_number, sort_code, balance):
    c = get_connection()
    c.cursor().execute(read_sql('insert_account.sql'), (name, account_number, sort_code, balance))
    c.commit()

def insert_transaction(sender_account_number, receiver_account_number, amount, payment_type):
    c = get_connection()
    c.cursor().execute(read_sql('insert_transaction.sql'), (sender_account_number, receiver_account_number, amount, payment_type))
    c.commit()

def update_balance(balance, account_number):
    c = get_connection()
    c.cursor().execute(read_sql('update_balance.sql'), (balance, account_number))
    c.commit()

def get_account(account_number):
    c = get_connection()
    row = c.cursor().execute(read_sql('get_account.sql'), (account_number,)).fetchone()
    return row