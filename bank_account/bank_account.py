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
        Initializes a client object based on the 
        received arguments (if valid).
        
        Args:
            account_number (int): An integer value representing the 
            bank account number.
            client_number (int):An integer value representing the
            client number representing the account holder.
            balance (float):A float value representing the 
            current balance of the bank account.
            
        Raises:
            ValueError: if any of the arguments are invalid.
            - account number is not numeric.
            - client number is not numeric.
            
        Notes:
            - If the argument of balance is float or int data type 
             then the attribute should assigned to the given argument.
             If the argument cannot converted to float then the 
             attribute representing the balance should be set to 0.
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
        
    @property
    def account_number (self) -> int:
        """
        Accessor for the account_number attribute.
        
        Returns: 
            int: An integer value representing the bank 
            account number.
        """
        return self.__account_number
    
    @property
    def client_number (self) -> int:
        """
        Accessor for the client_number attribute.
        
        Returns: 
            int: An integer value representing the client number 
            representing the account holder.
        """
        return self.__client_number
    
    @property
    def balance (self) -> float:
        """
        Accessor for the balance attribute.
        
        Returns:
            A float value representing the current balance of the 
            bank account.
        """
        return self.__balance
    
    def update_balance (self, amount: float):
        """   
        Updates the balance by adding the specified amount
        to the current balance (can be postive or negative).
        Ensures the amount is either an integer or a float.
        
        Args:
            amount (float): The amount to add to the balance.
        
        Returns:
            None: This method does not return anything.
        """
        if isinstance(amount, (float,int)):
            self.__balance += amount
            
    def deposit (self, amount: float):
        """
        Deposit an amount into the account.
        
        Args:
            amount (float): The amount to be deposit.
            
        Raises:
            ValueError: if the argument is invalid.
            - amount is not numeric.
            - amount is negative.
            
        Update the balance by calling update_balance function 
        if all the required conditions are met.
        
        Returns:
            None: This method does not return anyhting.
        """
        if not isinstance(amount, (float,int)):
            raise ValueError(f"Deposit amount: {amount}"
                            +f" must be numeric.")
        elif amount < 0:
            raise ValueError(f"Deposit amount: ${round(amount, 2)} "
                            +f"must be positive.")
        else:
            self.update_balance(amount)
            
    
    def withdraw(self, amount: float):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to be withdraw.
            
        Raises:
            ValueError: if the argument is invalid.
            - amount is not numeric.
            - amount is negative.
            
        Updates the balance by calling update_balance function 
        if all of the required conditions are met.
        
        Returns:
            None: This method does not return anything.
            
        """
        if not isinstance(amount, (float,int)):
            raise ValueError(f"Withdraw amount: {amount}"
                            +f" must be numeric.")    
        elif  amount < 0:
            raise ValueError(f"Withdraw amount: ${round(amount, 2)} "
                            +f"must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${round(amount, 2)}"
                        +f" must not exceed the account balance: "
                        +f"${round(self.__balance, 2)}")
        else:
            self.update_balance(-amount)
            
    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount instance.
        
        Returns: 
            str: The BankAccount instance as a formatted string.
        """
        return (f"Account Number: {self.__account_number}"
                +f" Balance: ${round(self.__balance, 2)}")
            
        