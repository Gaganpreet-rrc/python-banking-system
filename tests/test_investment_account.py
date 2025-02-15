"""
Description: Unit tests for the InvestmentAccount class.
Author: Gaganpreet Kaur
Date: 2025-02-14
Usage: To execute all tests in the terminal execute 
the following command (replace test_file_name.py with 
the appropriate file name.):
    python -m unittest tests/test_file_name.py
"""

#  IMPORT STATEMENTS
import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount


class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        self.investment_account = InvestmentAccount(12345678,
                                                    25,
                                                    900.2,
                                                    date(2024,2,10),
                                                    1.99)
        self.old_date = date.today() - timedelta(days = 11 * 365.25)
        self.exactly_ten = date.today() - timedelta(days = 10 * 365.25)
        self.new_date = date.today() - timedelta(days = 9 * 365.25)
        
            
    def test_init_valid_arguments_attributes_set(self):
        # verify superclass private attributes
        self.assertEqual(12345678,
            self.investment_account._BankAccount__account_number)
        self.assertEqual(25,
            self.investment_account._BankAccount__client_number)
        self.assertEqual(900.2,
            self.investment_account._BankAccount__balance)
        
        # verify superclass protected attributes
        self.assertEqual(date(2024,2,10), 
                         self.investment_account._date_created)
        
        # verify subclass private attributes
        self.assertEqual(1.99, 
            self.investment_account._InvestmentAccount__management_fee)
        
    def test_init_non_numeric_management_fee_assigns_value(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               date(2024,2,10),
                                               "20.2")
        # Assert
        self.assertEqual(2.55, 
            investment_account._InvestmentAccount__management_fee)
        
    def test_get_service_charges_when_date_created_more_than_ten_years_ago_returned(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               self.old_date,
                                               1.99)
        calculated_service = investment_account.get_service_charges()
        
        # Assert
        self.assertEqual(0.50, calculated_service)
        
    def test_get_service_charges_when_date_created_exactly_ten_years_ago_returned(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               self.exactly_ten,
                                               1.99)
        calculated_service = investment_account.get_service_charges()
        
        # Assert
        self.assertEqual(2.49, calculated_service) 
    
    def test_get_service_charges_when_date_created_within_ten_years_ago_returned(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               self.new_date,
                                               1.99)
        calculated_service = investment_account.get_service_charges()
        
        # Assert
        self.assertEqual(2.49, calculated_service)
        
    def test_str_when_account_created_more_than_10_years_ago(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               self.old_date,
                                               1.99)
        expected = ("Account Number: 12345678 Balance: $900.20\n"
                    +f"Date Created: 2014-02-15 Management Fee: "
                    +f"Waived Account Type: Investment")
        # Assert
        self.assertEqual(expected, str(investment_account))
        
    def test_str_when_account_created_within_10_years_ago(self):
        # Arrange & Act
        investment_account = InvestmentAccount(12345678,
                                               25,
                                               900.2,
                                               self.new_date,
                                               1.99)
        expected = ("Account Number: 12345678 Balance: $900.20\n"
                    +f"Date Created: 2016-02-15 Management Fee: "
                    +f"$1.99 Account Type: Investment")
        # Assert
        self.assertEqual(expected, str(investment_account))
    