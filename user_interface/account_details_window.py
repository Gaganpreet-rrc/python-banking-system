__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Gaganpreet Kaur"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
from copy import copy


class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)
    
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        if isinstance(account, BankAccount):
            self.__account = copy(account)
            self.account_number_label.setText(str(self.__account.account_number))
            self.balance_label.setText(f"${self.__account.balance:.2f}")
            
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()
        
    @Slot()       
    def __on_apply_transaction(self):
        """
        Handles deposit or withdrawal transactions when a button is clicked.
        - Validates the amount input.
        - Applies the appropriate transaction based on the sender.
        - Updates the displayed balance.
        - Emits a signal with the updated account.
        - Handles and displays any transaction-related exceptions.
        """
        
        try:
            amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.information(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(amount)
            self.balance_label.setText(f"${self.__account.balance:.2f}")
            self.balance_updated.emit(self.__account)
            
            self.transaction_amount_edit.clear()
            
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()
            
            self.transaction_amount_edit.setFocus()
            

    @Slot()
    def __on_exit(self):
        """
        Closes the Account Details window and returns control to the Client Lookup window.
        """
        self.close()
        