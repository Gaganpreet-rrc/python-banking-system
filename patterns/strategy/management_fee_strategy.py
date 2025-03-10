__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    
    """
    
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
    
    def __init__(self, date_created: date, management_fee: float):
        """
        
        """
        self.__date_created = date_created
        self.__management_fee = management_fee
        
        
    def get_service_charges(self) -> float:
        """
            
        """
        
        if self._date_created < self.TEN_YEARS_AGO:
            calculated_service_charge = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service_charge = (self.BASE_SERVICE_CHARGE +
                                  self.__management_fee)

        return calculated_service_charge

