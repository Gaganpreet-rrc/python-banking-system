__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    ManagementFeeStrategy: This strategy applies a fixed management fee 
    based on the account balance or other criteria.
    """
    
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    
    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes date_created and management_fee amount.  
        Args:
            date_created: The date when the account was created.
            management_fee: The fixed management fee to be applied.
        """
        
        self.__date_created = date_created
        self.__management_fee = management_fee
        
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charge for the account.
        
        Returns:
            float: The calculated service charge.
            
        Notes:
            If the account was created more than 10 years ago, only the 
            base service charge is applied. If the account was created
            10 years ago or less, the service charge includes both the
            base service charge and the management fee.
        """
        
        if self.__date_created < self.TEN_YEARS_AGO:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service_charge = (self.BASE_SERVICE_CHARGE +
                                  self.__management_fee)

        return calculated_service_charge

