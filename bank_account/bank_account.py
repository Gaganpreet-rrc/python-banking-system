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
        
        
    def account_number (self) -> int:
        """
        
        """
        return self.__account_number
    
    def client_number (self) -> int:
        """
        
        """
        return self.__client_number
    
    def balance (self) -> float:
        """
        
        """
        return self.__balance
    
    def update_balance (self, amount: float):
        """
        
        """
        if isinstance(amount, (float,int)):
            self.__balance += amount
            
    def deposit (self, amount: float):
        """
        
        """
        if not isinstance(amount, (float,int)):
            raise ValueError(f"Deposit amount: {amount}"
                            +f" must be numeric.")
        elif  amount < 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} "
                            +f"must be positive.")
        else:
            self.update_balance(amount)
            
    
    def withdraw(self, amount: float):
        """
        
        """
        if not isinstance(amount, (float,int)):
            raise ValueError(f"Withdraw amount: {amount}"
                            +f" must be numeric.")    
        elif  amount < 0:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} "
                            +f"must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f}"
                        +f"must not exceed the account balance: "
                        +f"${self.__balance:,.2f}")
        else:
            self.update_balance(-amount)
            
    def __str__(self) -> str:
        """
        
        """
        return (f"Account Number: {self.__account_number}"
                +f" Balance: ${self.__balance:,.2f}")
            
        