"""
Description: A class that represents saving account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"


from datetime import date

from bank_account.bank_account import BankAccount
from patterns.strategy.minimun_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):
    """
    SavingAccount class: Represents saving account 
    information of banking clients with a short-term
    savings plan.
    """
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date,
                 minimum_balance: float):
        """
        Initializes a savings account object based on the 
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
            minimum_balance (float): The minimum value a balance can
            be before further service charges are applied.
            
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
             
            - If the argument of minimum_balance is float data type 
             then the attribute should assigned to the given argument.
             If the argument cannot converted to float then the 
             attribute representing the minimum_balance should be
             set to 50
                 
        """
        super().__init__(account_number, client_number,
                         balance, date_created)
        
        if isinstance(minimum_balance,float):
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 50
            
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)
            
    def __str__(self) -> str:
        """
        Returns a string representation of a SavingsAccount object.

        Returns:
            str: Savings Account formatted as a string.
            
        """
        return_value = super().__str__()
        return_value += (f"Minimum Balance: "
                         +f"${self.__minimum_balance:,.2f} "
                         +f"Account Type: Savings")
        
        return (return_value)
        
    def get_service_charges(self) -> float:
        """
        Returns the service charge for the account based on 
        the assigned strategy.

        This method calls the strategy's `calculate_service_charges` 
        method to determine the service charge.

        Returns:
            The calculated service charge as a float.
        """
        return self.__strategy.calculate_service_charges(self)
    