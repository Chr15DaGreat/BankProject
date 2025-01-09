import sqlite3
import main

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

info = '''CREATE TABLE IF NOT EXISTS bankaccount (
  first_name TEXT,
  last_name TEXT,
  account_id INTEGER,
  account_type INTEGER,
  pin INTEGER,
  balance REAL
)'''

conn.execute(info)

