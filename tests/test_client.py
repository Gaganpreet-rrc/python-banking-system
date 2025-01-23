"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

# IMPORT STATEMENTS
import unittest
from client.client import Client
from email_validator import validate_email, EmailNotValidError

class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.client = Client(10, 
                             "Raman",
                             "Kaur",
                             "raman@pixell-river.com")
    
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        client = Client(10, "Raman", "Kaur", "raman@pixell-river.com")
        # Assert
        self.assertEqual(10, client._Client__client_number)
        self.assertEqual("Raman", client._Client__first_name)
        self.assertEqual("Kaur", client._Client__last_name)
        self.assertEqual("raman@pixell-river.com",
                         client._Client__email_address)
        
    def test_init_invalid_client_number_raises_ValueError(self):
        # Arrange , Act and Assert
        with self.assertRaises(ValueError):
          client = Client("10", 
                          "Raman",
                          "Kaur",
                          "raman@pixell-river.com")  
          
    
    def test_init_blank_first_name_raises_ValueError(self):
        # Arrange , Act and Assert
        with self.assertRaises(ValueError):
          client = Client(10, "", "Kaur", "raman@pixell-river.com")  

        
    def test_init_blank_last_name_raises_ValueError(self):
        # Arrange , Act and Assert
        with self.assertRaises(ValueError):
          client = Client(10, "Raman", "", "raman@pixell-river.com")
      
          
    def test_init_invalid_email_set_by_default(self):
        # Arrange
          client = Client(10, "Raman", "Kaur", "INVALID")
          expected = "email@pixell-river.com"
        # Act and Assert
          self.assertEqual(expected, client.email_address)
          
          
    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange , Act and Assert
        self.assertEqual(10, self.client.client_number)
        
        
    def test_first_name_accessor_valid_client_name_returned(self):
        # Arrange , Act and Assert
        self.assertEqual("Raman", self.client.first_name)
        
        
    def test_last_name_accessor_valid_client_name_returned(self):
        # Arrange , Act and Assert
        self.assertEqual("Kaur", self.client.last_name)
        
        
    def test_email_address_accessor_valid_email_returned(self):
        # Arrange , Act and Assert
        self.assertEqual("raman@pixell-river.com",
                         self.client.email_address)        
        
        
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Kaur, Raman [10] - raman@pixell-river.com")
        # Act and Assert
        self.assertEqual(expected, str(self.client))
    
    