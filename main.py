import sqlite3

class bankaccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance

  def display_balance(self):
    return self.balance

first_name = input('What is your name?\n').lower()
last_name = input('What is your last name?\n').lower()
account_id = int(input('What is your account ID?\n'))
account_type = int(input('Press 1 if it is a chequing account, 2 if it is an investment account, and 3 if it is a credit account.\n'))
pin = int(input('What is your pin?\n'))
if pin < 0 and pin > 9999:
  print('Error, your pin must be 4 digits')
  quit()
balance = float(input('What is your balance?\n'))
if balance < 0:
  print('Error, you cannot have negative balance')
  quit()

info = bankaccount(first_name, last_name, account_id, account_type, pin, balance)
using = 1

print('Welcome to the bank, ' + info.first_name + ' ' + info.last_name + '!')

while using == 1:
  type = int(input('Type 1 for deposit, 2 for withdrawal, and 3 for balance.\n'))
  if type == 1:
    amount = float(input('How much would you like to deposit?\n'))
    print('Your new balance is ' + str(info.deposit(amount)))
    using = int(input('Thank you for your deposit, type 1 if you want to continue using, or type 2 to exit.\n'))
    
  elif type == 2:
    amount = float(input('How much would you like to withdraw?\n'))
    if amount > info.balance:
      print('You do not have enough money in your account.')
    else:
      print('Your new balance is ' + str(info.withdraw(amount)))
      using = int(input('Thank you for your deposit, type 1 if you want to continue using, or type 2 to exit.\n'))
    
  else:
    print('Your balance is ' + str(info.display_balance()))
    using = int(input('Thank you for your deposit, type 1 if you want to continue using, or type 2 to exit.\n'))

print('Thank you for using the bank')