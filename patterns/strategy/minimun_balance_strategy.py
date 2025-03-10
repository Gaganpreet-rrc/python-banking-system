__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    MinimumBalanceStrategy: This strategy applies a service charge
    based on whether the balance of the account meets or exceeds
    the minimum balance threshold.
    If the balance is below the minimum, a premium service charge
    is applied.
    """
    
    SERVICE_CHARGE_PREMIUM: float = 2.0
    
    def __init__(self, minimum_balance: float):
        """
        Initializes the minimum balance for the strategy.
        
        Args:
            minimum_balance (float): The minimum balance required to avoid a service charge.
        """
        self.__minimum_balance = minimum_balance
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charge for the account.
        
        Returns:
            float: The calculated service charge.
            
        Notes:
            If the balance is greater than or equal to minimum balance,
            then the service charge set to BASE_SERVICE_CHARGE value.
            If the balance is less than minimum balance, then the
            service charge is calculated through a given formula.
        """
        
        if account.balance >= self.__minimum_balance:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
        else:
            calculated_service_charge = (self.BASE_SERVICE_CHARGE *
                                        self.SERVICE_CHARGE_PREMIUM)
            
        return calculated_service_charge
        
        
        