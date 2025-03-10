__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        
        """
        
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        
    def get_service_charges(self) -> float:
        """
        
        """
        if self.balance >= self.__overdraft_limit:
            calculated_service = self.BASE_SERVICE_CHARGE
            
        else:
            calculated_service = (self.BASE_SERVICE_CHARGE +
            (self.__overdraft_limit - self.balance) *  
            self.__overdraft_rate)
            
        return calculated_service