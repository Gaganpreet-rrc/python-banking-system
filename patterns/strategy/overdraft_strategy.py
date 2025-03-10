__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    OverdraftStrategy: This class inherited from ServiceChargeStrategy
    class strategy and it calculates a service charge when the
    account balance goes into an overdraft.
    """
    
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the overdraft limit and charge rate for 
        calculating overdraft charges.
        
        Args:
            overdraft_limit (float): The balance limit at which 
            overdraft charges apply.
            overdraft_rate (float): The rate to apply when the
            account goes into overdraft.
        
        """
        
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charges based on the account's balance
        and overdraft limit.
        
        Args:
            account (BankAccount): It receives service charge based
            on BankAccount instance. 

        Returns:
            float: The calculated service charge.
            
        Notes:
            If the balance is greater than or equal to the overdraft limit, 
            the base service charge is applied. Otherwise, an 
            additional charge is added based on the overdraft
            rate and the exceeded amount.
        """
        
        if account.balance >= self.__overdraft_limit:
            calculated_service = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service = (self.BASE_SERVICE_CHARGE +
            (self.__overdraft_limit - account.balance) *  
            self.__overdraft_rate)
            
        return calculated_service