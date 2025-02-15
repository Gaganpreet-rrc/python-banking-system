"""
Description: A class that represents saving account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

# IMPORT STATEMENTS
from datetime import date

from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    SavingAccount class: Represents saving account 
    information of banking clients with a short-term
    savings plan.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0 #Constant variable
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 minimum_balance: float):
        """
        
        """
        super().__init__(account_number, client_number,
                         balance, date_created)
        
        if isinstance(minimum_balance,float):
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 50
            
    def __str__(self) -> str:
        """
        
        """
        return_value = super().__str__()
        return_value += (f"Minimum Balance: "
                         +f"{self.__minimum_balance:,.2f} "
                         +f"Account Type: Savings")
        
    def get_service_charges(self) -> float:
        """
        
        """
        if self.__balance >= self.__minimum_balance:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
        else:
            calculated_service_charge = (self.BASE_SERVICE_CHARGE *
                                        self.SERVICE_CHARGE_PREMIUM)
            
        return calculated_service_charge
            
            