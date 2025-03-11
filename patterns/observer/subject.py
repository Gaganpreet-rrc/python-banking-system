__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from observer.observer import Observer

class Subject(ABC):
    """
    Subject: This is an abstract class. This class is responsible
    for maintaining a list of its observers and notifying them
    of state changes or events.
    """
    
    def __init__(self):
        """
        Initializes the subject object with an empty list of observers.
        """
        self._observers: list[Observer] = []
        
    @abstractmethod
    def attach(self, observer: Observer):
        """
        Adds an observer to the list of observers.

        Args:
            observer (Observer): The observer to be added.  
        """
        pass
        
    @abstractmethod
    def detach(self, observer: Observer):
        """
        Removes an observer from the list.
        
        Args:
            observer (Observer): The observer to be removed.
        """
        self._observers.remove
    
    @abstractmethod
    def notify(self, message: str):
        """
        Notifies all observers with a message.
        
        Args:
            message (str): The update message.
        """
        pass
        
        