"""
Description: Unit tests for the ChequingAccount class.
Author: Gaganpreet Kaur
Date: 2025-02-13
Usage: To execute all tests in the terminal execute 
the following command (replace test_file_name.py with 
the appropriate file name.):
    python -m unittest tests/test_file_name.py
"""

#  IMPORT STATEMENTS
import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    
    def setUp(self):
        self.chequing_account = ChequingAccount(12345678,
                                                25,
                                                900.2,
                                                date(2024,2,10),
                                                5.5,
                                                0.025)
        
    def test_init_valid_arguments_attributes_set(self):
        # verify superclass private attributes
        self.assertEqual(12345678,
                    self.chequing_account._BankAccount__account_number)
        self.assertEqual(25,
                    self.chequing_account._BankAccount__client_number)
        self.assertEqual(900.2,
                    self.chequing_account._BankAccount__balance)
        
        # verify superclass protected attributes
        self.assertEqual(date(2024,2,10), 
                         self.chequing_account._date_created)
        
        # verify subclass private attributes
        self.assertEqual(5.5,
            self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.025, 
                self.chequing_account._ChequingAccount__overdraft_rate)
        
    def test_init_non_numeric_overdraft_limit_assigns_value(self):
        # Arrange & Act
        chequing_account = ChequingAccount(12345678,
                                           25,
                                           900.2,
                                           date(2024,2,10),
                                           "10.0",
                                           0.025)
        # Assert
        self.assertEqual(-100, 
            chequing_account._ChequingAccount__overdraft_limit)

    def test_init_non_numeric_overdraft_rate_assigns_value(self):
        # Arrange & Act
        chequing_account = ChequingAccount(12345678,
                                           25,
                                           900.2,
                                           date(2024,2,10),
                                           5.5,
                                           "20")
        # Assert
        self.assertEqual(0.05, 
                chequing_account._ChequingAccount__overdraft_rate)
        
    
    def test_init_invalid_date_created_assigns_current_date(self):
        # Arrange & Act
        chequing_account = ChequingAccount(12345678,
                                           25,
                                           900.2,
                                           "2024-02-10",
                                           5.5,
                                           0.025)
        # Assert
        self.assertEqual(date.today(), 
                         chequing_account._date_created)
        
        
    def test_get_service_charges_when_balance_exceeds_overdraft_limit_returned(self):
        # Arrange and Act
        calculated_service =self.chequing_account.get_service_charges()
        
        # Assert
        self.assertEqual(0.50, calculated_service)
        
    def test_get_service_charges_when_balance_less_than_overdraft_limit_returned(self):
        # Arrange and Act
        chequing_account = ChequingAccount(12345678,
                                           25,
                                           200.2,
                                           date(2024,2,10),
                                           500.5,
                                           0.025)
        calculated_service = chequing_account.get_service_charges()
        # Assert
        self.assertEqual(8.0075, calculated_service)
        
    def test_get_service_charges_when_balance_equal_overdraft_limit_returned(self):
        # Arrange and Act
        chequing_account = ChequingAccount(12345678,
                                           25,
                                           900.2,
                                           date(2024,2,10),
                                           900.2,
                                           0.025)
        
        calculated_service = chequing_account.get_service_charges()
        # Assert
        self.assertEqual(0.50, calculated_service)  
    
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 12345678 Balance: $900.20\n"
                    +f"Overdraft Limit: $5.50 Overdraft Rate: "
                    +f"0.03% Account Type: Chequing")
        
        # Act and Assert
        self.assertEqual(expected, str(self.chequing_account))
        