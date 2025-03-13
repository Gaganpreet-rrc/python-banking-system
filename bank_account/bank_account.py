"""
Description: A class that represents bank account.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject


class BankAccount(Subject, ABC):
    """
    BankAccount class. Represents bank account information of clients.
    """
    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0
    
    def __init__(self,
                 account_number: int,
                 client_number: int,
                 balance: float,
                 date_created: date):
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
            date_created (date): The date when the bank account
            was created.
            
            
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
        """
        super().__init__()
        
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
            
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()
        
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
        Updates the balance by adding the given amount. 

        Args:
            amount (float): The transaction amount.

        Notifications:
            - Sends a low balance warning if balance
              falls below LOW_BALANCE_LEVEL.
            - Sends an alert for transactions exceeding
              LARGE_TRANSACTION_THRESHOLD.
        
        Returns:
            None: This method does not return anything.
        """
        self.__balance += amount
        if self.__balance < self.LOW_BALANCE_LEVEL:
            
            message = (f"Low balance warning ${self.__balance:,.2f}: "
            +f"on account {self.__account_number}.")
            
            self.notify(message)
            
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            
            message_2 = (f"Large transaction ${amount:,.2f}: "
            +f"on account {self.__account_number}.")
            
            self.notify(message_2)

            
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
            raise ValueError(f"Withdraw amount: ${amount:,.2f} "
                            +f"must be positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f}"
                        +f" must not exceed the account balance: "
                        +f"${self.__balance:,.2f}")
        else:
            self.update_balance(-amount)
            
    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount instance.
        
        Returns: 
            str: The BankAccount instance as a formatted string.
            
        """
        return (f"Account Number: {self.__account_number}"
                +f" Balance: ${self.__balance:,.2f}\n")
        
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculate service charges based on the type of BankAccount.
        Implemented in subclass(es).
        
        Returns:
            float: The calculated service charge.
        """
        pass
    
    def attach(self, observer: Observer):
        """
        Adds an observer to the subject's list of observers.

        Args:
            observer (Observer): The observer instance to be added.
        """
        self._observers.append(observer)
       
        
    def detach(self, observer: Observer):
        """
        Removes an observer from the subject's list of observers.

        Args:
            observer (Observer): The observer instance to be removed.
        """
        self._observers.remove(observer)
        
    
    def notify(self, message: str):
        """
        Notifies all registered observers of a state change.

        Args:
            message (str): The message to be sent to all observers.
        """
        for observer in self._observers:
            observer.update(message)
        