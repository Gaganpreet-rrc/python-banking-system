"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Gaganpreet Kaur"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date, timedelta

old_date = date.today() - timedelta(days = 11 * 365.25)
exactly_ten = date.today() - timedelta(days = 10 * 365.25)
new_date = date.today() - timedelta(days = 9 * 365.25)

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(12345678,
                                       25,
                                       20.2,
                                       date(2024,2,10),
                                       50.5,
                                       0.025)
except Exception as e:
    print(e)
    

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
print(chequing_account.get_service_charges())


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

try:
    chequing_account.deposit(200.0)
    print(chequing_account)
    print(chequing_account.get_service_charges())
except Exception as e:
    print(e)
    

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(12345678,
                                     25,
                                     900.2,
                                     date(2024,2,10),
                                     100.0)
except Exception as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
print(savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    savings_account.withdraw(850.2)
    print(savings_account)
    print(savings_account.get_service_charges())
except Exception as e:
    print(e)


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account_within_ten_years = InvestmentAccount(12345678,
                                           25,
                                           900.2,
                                           new_date,
                                           1.99)
except Exception as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account_within_ten_years)
print(investment_account_within_ten_years.get_service_charges())


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account_prior_ten_years = InvestmentAccount(12345678,
                                           25,
                                           900.2,
                                           old_date,
                                           1.99)
except Exception as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account_prior_ten_years)
print(investment_account_prior_ten_years.get_service_charges())


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5,
# 8 and 10 by using the withdraw method of the superclass and  
# withdrawingthe service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    withdraw_amount_chequing = chequing_account.get_service_charges()
    chequing_account.withdraw(withdraw_amount_chequing)
    
    withdraw_amount_savings = savings_account.get_service_charges()
    savings_account.withdraw(withdraw_amount_savings)
    
    withdraw_amount_investment_within = investment_account_within_ten_years.get_service_charges()
    investment_account_within_ten_years.withdraw(withdraw_amount_investment_within)
    
    withdraw_amount_investment_prior = investment_account_prior_ten_years.get_service_charges()
    investment_account_prior_ten_years.withdraw(withdraw_amount_investment_prior)
    
except Exception as e:
    print(e)

# 13. Print each of the bank account objects 
# created in steps 2, 5, 8 and 10.
print(chequing_account)
print(savings_account)
print(investment_account_within_ten_years)
print(investment_account_prior_ten_years)
