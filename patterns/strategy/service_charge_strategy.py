__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    ServiceChargeStrategy: This is an abstract class that defines 
    a strategy for calculating service charges. 
    
    """
    BASE_SERVICE_CHARGE: float = 0.50
    
    @abstractmethod
    def calculate_service_charges(self, account: BankAccount)-> float:
        """
        Abstract method to calculate the service charge based
        on balance.
        
        Args:
            account (BankAccount): It receives service charge based
            on BankAccount instance. 
            
        Returns:
            float: Calculate service charge.

        """
        
        pass