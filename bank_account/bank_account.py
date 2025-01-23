"""
Description: A class that represents bank account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"


class BankAccount:
    """
    BankAccount class. Represents bank account information of clients.
    """
    
    def __init__(self, 
                 account_number: int,
                 client_number: int,
                 balance: float):
        """
        
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        
        if isinstance(balance, (float,int)):
            self.__balance = balance
        else:
            self.__balance = 0
        
        
        