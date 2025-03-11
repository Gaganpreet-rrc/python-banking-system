__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer (Interface): A base class for observers in the
    Observer pattern.
    
    This class defines the method that all observers must implement 
    to receive updates from a subject.
    """
    
    @abstractmethod
    def update(message: str):
        """
        Receives updates from the subject.
        
        Args:
            message (str): The update message sent by the subject.
        """
        pass
    
