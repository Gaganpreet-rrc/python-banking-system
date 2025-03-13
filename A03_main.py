"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Gaganpreet Kaur"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount
from datetime import date
from client.client import Client



# 2. Create a Client object with data of your choice.
try:
    client = Client(12345,
                    "Gaganpreet",
                    "Kaur",
                    "gaganpreetkaur22@gmail.com")
except ValueError as e:
    print(e)


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

try:
    chequing_account = ChequingAccount(1234567,
                                       client.client_number,
                                       200.2,
                                       date(2024,2,10),
                                       50.5,
                                       0.025)
except ValueError as e:
    print(e)

try:
    savings_account = SavingsAccount(8543267,
                                     client.client_number,
                                     900.2,
                                     date(2024,2,10),
                                     100.0)
except ValueError as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

chequing_account.attach(client)
savings_account.attach(client)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_2 = Client(234567,
                      "Anand",
                      "Kaur",
                      "anandkaur44@gmail.com")
except ValueError as e:
    print(e)

try:
    savings_account_2 = SavingsAccount(6785435,
                                      client_2.client_number,
                                      700.6,
                                      date(2024,10,10),
                                      50.0)
except ValueError as e:
    print(e)
    

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    chequing_account.withdraw(160.0)  
except ValueError as e:
    print(e)
    
try:
    chequing_account.deposit(10000.0)  
except ValueError as e:
    print(e)
    
try:
    chequing_account.withdraw(10000.0) 
except ValueError as e:
    print(e)
    
try:
    savings_account.withdraw(860.2) 
except ValueError as e:
    print(e)
    
try:
    savings_account.deposit(50000.0) 
except ValueError as e:
    print(e)
    
try:
    savings_account.withdraw(440000.2)
except ValueError as e:
    print(e)
        
try:
    savings_account_2.withdraw(700.0) 
except ValueError as e:
    print(e)

try:
    savings_account_2.deposit(45000.0)
except ValueError as e:
    print(e)
    
try:
    savings_account_2.withdraw(55000.0) 
except ValueError as e:
    print(e)
    