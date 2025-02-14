"""
Description: A class that represents investment account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

# IMPORT STATEMENTS
from datetime import date, timedelta

from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Represents investment account 
    information of banking clients who have deposited funds
    in the investment Account.
    """
        
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25) # Constant variable
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 management_fee: float):
        """
        
        """
        
        super().__init__(account_number, client_number,
                         balance, date_created)
        
        if isinstance(management_fee, float):
            self.__management_fee = management_fee
        else:
            self.__management_fee = 2.55
            
    def __str__(self) -> str:
        """
            
        """
        return_value = super().__str__()
        if self._date_created <= self.TEN_YEARS_AGO:
            fee = f"${self.__management_fee:.2f}"
        else:
            fee = "waived"
            
        return_value += (f"Date Created: {self._date_created} "
                         +f"Management Fee: {fee} Account Type: "
                         +f"Investment")
        
        return return_value
    
    def get_service_charges(self) -> float:
        """
        
        """
        if self._date_created > self.TEN_YEARS_AGO:
            calculated_service = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service = (self.BASE_SERVICE_CHARGE +
                                  self.__management_fee)
            
        return calculated_service
    