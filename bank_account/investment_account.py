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
        
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 management_fee: float):
        """
        Initializes a investment account object based on the 
        received arguments (if valid).
        
        Args:
            account_number (int): An integer value representing the 
            bank account number.
            client_number (int):An integer value representing the
            client number representing the account holder.
            balance (float):A float value representing the 
            current balance of the bank account.
            date_created (date): The date when the bank account
            was created.
            management_fee (float): The management_fee is a float which
            stores a flat-rate fee the bank charges for managing an
            InvestmentAccount.
            
        Raises:
            ValueError: if any of the arguments are invalid.
            - account number is not numeric.
            - client number is not numeric.
            
        Notes:
            - If the argument of balance is float or int data type 
             then the attribute should assigned to the given argument.
             If the argument cannot converted to float then the 
             attribute representing the balance should be set to 0.
             
            - If the argument of date_created is date type then the 
             the attribute should assigned to the given argument.
             If the argument is not of date type then the attribute 
             should assigned to the current date.
             
            - If the argument of management_fee is float data type 
             then the attribute should assigned to the given argument.
             If the argument cannot converted to float then the 
             attribute representing the management_fee should be
             set to 2.55.
             
        """
        
        super().__init__(account_number, client_number,
                         balance, date_created)
        
        if isinstance(management_fee, float):
            self.__management_fee = management_fee
        else:
            self.__management_fee = 2.55
            
    def __str__(self) -> str:
        """
        Returns a string representation of a InvestmentAccount object.

        Returns:
            str: Investment Account formatted as a string.
            
        """
        return_value = super().__str__()
        if self._date_created >= self.TEN_YEARS_AGO:
            fee = f"${self.__management_fee:,.2f}"
        else:
            fee = "Waived"
            
        return_value += (f"Date Created: {self._date_created} "
                         +f"Management Fee: {fee} Account Type: "
                         +f"Investment")
        
        return return_value
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge for the investment account.
        
        Returns:
            float: The calculated service charge.
            
        Notes:
            If the account was created more than 10 years ago, only the 
            base service charge is applied. If the account was created
            10 years ago or less, the service charge includes both the
            base service charge and the management fee.
            
        """
        if self._date_created < self.TEN_YEARS_AGO:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service_charge = (self.BASE_SERVICE_CHARGE +
                                  self.__management_fee)

        return calculated_service_charge
    