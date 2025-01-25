"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

# IMPORT STATEMENTS
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.bank_account = BankAccount(12345678, 25, 900.2)
        
    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(12345678, 25, 900.1)
        # Assert
        
        self.assertEqual(12345678, 
                         bank_account._BankAccount__account_number)
        self.assertEqual(25, bank_account._BankAccount__client_number)
        self.assertEqual(900.1, bank_account._BankAccount__balance)
        
    def test_init_invalid_balance_argument_set_to_0_by_default(self):
        # Arrange & Act
        bank_account = BankAccount(12345678, 25, "20")
        expected = 0
        # Assert
        
        self.assertEqual(expected, bank_account.balance)
        
    def test_init_non_numeric_account_number_raises_ValueError(self):
        # Arrange , Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("2345", 25, 900.2)
            
    def test_init_non_numeric_client_number_raises_ValueError(self):
        # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(12345678, "45", 900.2)
            
    def test_account_number_accessor_valid_account_number_returned(self):
        # Arrange , Act and Assert
        self.assertEqual(12345678, self.bank_account.account_number)
        
    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange , Act and Assert
        self.assertEqual(25, self.bank_account.client_number)
        
    def test_balance_accessor_valid_balance_returned(self):
        # Arrange , Act and Assert
        self.assertEqual(900.2, self.bank_account.balance)
        
    def test_update_balance_valid_positive_amount_received(self):
        # Arrange
        initial_balance = 900.2
        amount = 10.0
        expected = 910.2
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act
        bank_account.update_balance(amount)
        
        # Assert
        self.assertEqual(expected, bank_account.balance)
        
    def test_update_balance_valid_negative_amount_received(self):
        # Arrange
        initial_balance = 900.2
        amount = -20
        expected = 880.2
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act
        bank_account.update_balance(amount)
        
        # Assert
        self.assertEqual(expected, bank_account.balance)
        
    def test_update_balance_non_numeric_amount_received(self):
        # Arrange
        initial_balance = 900.2
        amount = "50"
        expected = 900.2
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act
        bank_account.update_balance(amount)
        
        # Assert
        self.assertEqual(expected, bank_account.balance)
        
    def test_deposit_valid_amount_received(self):
        # Arrange
        initial_balance = 900.2
        amount = 100
        expected = 1000.2
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act
        bank_account.update_balance(amount)
        
        # Assert
        self.assertEqual(expected, bank_account.balance)
        
    def test_deposit_negative_amount_invalid_raises_ValueError(self):
        # Arrange
        initial_balance = 900.2
        amount = -20
        expected = f"Deposit amount: ${round(amount, 2)} must be positive." 
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            bank_account.deposit(amount)
            
        self.assertEqual(expected, str(context.exception))
            
    def test_deposit_non_numeric_amount_received_raises_ValueError(self):
        # Arrange
        initial_balance = 900.2
        amount = "50"
        expected = f"Deposit amount: {amount} must be numeric."
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            bank_account.deposit(amount)
            
        self.assertEqual(expected, str(context.exception))
        
    def test_withdraw_valid_amount_received(self):
        # Arrange
        initial_balance = 900.2
        amount = 40
        expected = 860.2
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act
        bank_account.update_balance(-amount)
        
        # Assert
        self.assertEqual(expected, bank_account.balance)
        
    def test_withdraw_negative_amount_received_raises_ValueError(self):
        # Arrange
        initial_balance = 900.2
        amount = -15
        expected = f"Withdraw amount: ${round(amount, 2)} must be positive."
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(amount)
            
        self.assertEqual(expected, str(context.exception))
        
    def test_withdraw_non_numeric_amount_received_raises_ValueError(self):
        # Arrange
        initial_balance = 900.2
        amount = "66"
        expected = f"Withdraw amount: {amount} must be numeric."
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(amount)
            
        self.assertEqual(expected, str(context.exception))
        
    
    
    def test_withdraw_amount_exceeds_balance_raises_ValueError(self):
        # Arrange
        initial_balance = 900.2
        amount = 5000
        expected = f"Withdrawal amount: ${round(amount, 2)} must not exceed the account balance: ${round(initial_balance, 2)}"
                        
        bank_account = BankAccount(12345678, 25, initial_balance)
        
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(amount)
            
        self.assertEqual(expected, str(context.exception))
        
    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = "Account Number: 12345678 Balance: $900.2"
        # Act and Assert
        self.assertEqual(expected, str(self.bank_account))
        