"""
Description: A class that represents client information.
"""
__author__ = "Gaganpreet Kaur"
__version__ = "1.0.0"

# IMPORT STATEMENTS
from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Client class. Represents clients information.
    """
    def __init__(self, 
                 client_number: int,
                 first_name: str,
                 last_name: str,
                 email_address: str):
        """
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")
        else:
            self.__first_name = first_name
            
            
        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank.")
        else:
            self.__last_name = last_name
            
            
        try:
            validated_email = validate_email(email_address,
                                             check_deliverability = False)
            self.__email_address = validated_email.display_name
            
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"