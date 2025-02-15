"""
Description: Unit tests for the SavingsAccount class.
Author: Gaganpreet Kaur
Date: 2025-02-14
Usage: To execute all tests in the terminal execute 
the following command (replace test_file_name.py with 
the appropriate file name.):
    python -m unittest tests/test_file_name.py
"""

#  IMPORT STATEMENTS
import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings_account = SavingsAccount(12345678,
                                              25,
                                              900.2,
                                              date(2024,2,10),
                                              100.0)
    
    def test_init_valid_arguments_attributes_set(self):
        # verify superclass private attributes
        self.assertEqual(12345678,
            self.savings_account._BankAccount__account_number)
        self.assertEqual(25,
            self.savings_account._BankAccount__client_number)
        self.assertEqual(900.2,
            self.savings_account._BankAccount__balance)
        
        # verify superclass protected attributes
        self.assertEqual(date(2024,2,10), 
                         self.savings_account._date_created)
        
        # verify subclass private attributes
        self.assertEqual(100.0, 
                self.savings_account._SavingsAccount__minimum_balance)
        
    def test_init_non_numeric_minimum_balance_assigns_value(self):
        # Arrange & Act
        savings_account = SavingsAccount(12345678,
                                         25,
                                         900.2,
                                         date(2024,2,10),
                                         "80.0")
        # Assert
        self.assertEqual(50, 
                    savings_account._SavingsAccount__minimum_balance)
        
        
    def test_get_service_charges_above_min_balance(self):
        # Arrange & Act
        calculated_service = self.savings_account.get_service_charges()
        # Assert
        self.assertEqual(0.50, calculated_service)
        
    def test_get_service_charges_equal_min_balance(self):
        # Arrange & Act
        savings_account = SavingsAccount(12345678,
                                         25,
                                         900.2,
                                         date(2024,2,10),
                                         900.2)
        calculated_service = savings_account.get_service_charges()
        # Assert
        self.assertEqual(0.50, calculated_service)


    def test_get_service_charges_below_min_balance(self):
        # Arrange & Act
        savings_account = SavingsAccount(12345678,
                                         25,
                                         100.2,
                                         date(2024,2,10),
                                         200.2)
        calculated_service = savings_account.get_service_charges()
        # Assert
        self.assertEqual(1.00, calculated_service)
        
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 12345678 Balance: $900.20\n"
                    +f"Minimum Balance: $100.00 Account Type: Savings")
        
        # Act and Assert
        self.assertEqual(expected, str(self.savings_account))
        