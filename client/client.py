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
        Initializes a client object based on the received
        arguments (if valid).
        
        Args:
            client_number (int): An integer value representing 
            the client number. 
            first_name (str): A string value the client's first name.
            last_name (str): A string value the client's last name.
            email_address (str): A string value the client's email 
            address.
            
        Raises:
            ValueError: if any of the arguments are invalid.
                - client_number is not an integer
                - first_name is blank
                - last_name is blank
        
        Notes:
            - The email address is validated by the function called
              validate_email
              but if the email is invalid then by default a valid 
              email will be assigned to it.
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
            self.__email_address = validated_email.normalized
            
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"
            
    @property
    def client_number(self) -> int:
        """
        Accessor for the client_number attribute.
        
        Returns:
            int: The client_number associated with the 
            Client instance.
        """
        return self.__client_number
        
    @property
    def first_name (self) -> str:
        """
        Accessor for the first_name attribute.
        
        Returns:
            str: The first name of the Client instance.
        """
        return self.__first_name
        
    @property
    def last_name (self) -> str:
        """
        Accessor for the last_name attribute.
        
        Returns:
            str: The last name of the Client instance.
        """
        return self.__last_name
        
    @property
    def email_address (self) -> str:
        """
        Accessor for the email_address attribute.
        
        Returns:
            str: The email_address of the Client instance.
        """
        return self.__email_address
        
        
    def __str__ (self) -> str:
        """
        Returns a string representation of the Client instance.
        
        Returns: 
            The Client instance as a formatted string.
        """
        return (f"{self.__last_name}, "
                + f"{self.__first_name} "
                + f"[{self.__client_number}] "
                + f"- {self.__email_address}")