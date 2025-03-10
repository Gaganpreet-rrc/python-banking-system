__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    

    """
    service_charge = BankAccount.BASE_SERVICE_CHARGE
    
    @abstractmethod
    def calculate_service_charges(account: BankAccount)-> float:
        """
        
        """
        pass