"""
Description: A class that represents Chequing account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

# IMPORT STATEMENTS
from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    ChequingAccount class. Represents Chequing account information
    of banking clients who has frequent transactions of both deposits
    and withdraws.
    """
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 overdraft_limit: float,
                 overdraft_rate: float):
        """
        
        """
        super().__init__(account_number, client_number,
                         balance, date_created) 
        
        if isinstance(overdraft_limit, float):
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100
            
        if isinstance(overdraft_rate, float):
            self.__overdraft_rate = overdraft_rate
        else:
            self.__overdraft_rate = 0.05
            
            
    def __str__(self) -> str:
        """
        
        """
        return_value = super().__str__()
        return_value += f"Overdraft Limit: "
        +f"${self.__overdraft_limit:.2f} Overdraft Rate: "
        +f"{self.__overdraft_rate:.2f}% Account Type: Chequing"
        
        return (return_value)
    
    def get_service_charges(self) -> float:
        """
        
        """
        if self.__balance >= self.__overdraft_limit:
            calculated_service = self.BASE_SERVICE_CHARGE
        else:
            calculated_service = (self.BASE_SERVICE_CHARGE +
            (self.__overdraft_limit - self.__balance) *  
            self.__overdraft_rate)
            
        return calculated_service
        