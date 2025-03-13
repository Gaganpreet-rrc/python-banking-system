"""
Description: A class that represents Chequing account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"


from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

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
                 overdraft_rate: float,
                 ):
        """
        Initializes a checking account object based on the 
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
            overdraft_limit (float): The maximum amount a balance can
            be overdrawn (below 0.00) before overdraft fees are applied.
            overdraft_rate (float):  The rate to which overdraft fees
            will be applied.
            
            
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
             
             - If the argument of overdraft_limit is float data type
             then the attribute should assigned to the given argument.
             - If the argument cannot converted to float then the 
             attribute representing the overdraft_limit 
             should be set to -100.
            
             - If the argument of overdraft_rate is float data type
             then the attribute should assigned to the given argument.
             - If the argument cannot converted to float then the 
             attribute representing the overdraft_rate 
             should be set to 0.05.
             
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
            
        self.__strategy = OverdraftStrategy(self.__overdraft_limit,
                                            self.__overdraft_rate)
            

    def __str__(self) -> str:
        """
        Returns a string representation of a CheckingAccount object.

        Returns:
            str: Checking Account formatted as a string.
            
        """
        return_value = super().__str__()
        return_value += (f"Overdraft Limit: "
        +f"${self.__overdraft_limit:.2f} Overdraft Rate: "
        +f"{self.__overdraft_rate:.2f}% Account Type: Chequing")
        
        return (return_value)
    
    def get_service_charges(self) -> float:
        """
        Retrieves the service charges for the current account
        based on the strategy for calculating the service charges.

        Returns:
            The service charge calculated based on the current
            strategy.
        """
        
        return self.__strategy.calculate_service_charges(self)
    
    
    