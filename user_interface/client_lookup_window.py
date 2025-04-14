__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Gaganpreet Kaur"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount
from client.client import Client

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        """
        Initializes a new instance of the ClientLookupWindow.

        This sets up the UI components and connects signals
        to their respective slots.
        """
        super().__init__()
        
        self.__client_listing, self.__accounts = load_data()
        
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
        
    @Slot()
    def __on_lookup_client(self):
        """
        Handles the client lookup when the user enters a client number.

        - Validates that the input is numeric.
        - Displays an error message if the client number is not found.
        - If found, displays client information and their related accounts
        in the account_table with details like account number, balance,
        date created, and account type.

        """
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.information(self, "Input Error",
                        "The client number must be a numeric value.")
            self.reset_display()
            return
        
        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found",
                        f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        else:
            match_client = self.__client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {match_client.first_name} {match_client.last_name}")
            
            self.account_table.setRowCount(0)
            
        for account in self.__accounts.values():
            if match_client.client_number == client_number:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                
                account_number_item = \
                QTableWidgetItem(str(account.account_number))
                balance = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = \
                QTableWidgetItem(account._date_created.strftime("%Y-%m-%d")) 
                account_type_item = \
                QTableWidgetItem(account.__class__.__name__) 
                
                balance.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_number_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)
 
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)
                
        self.account_table.resizeColumnsToContents()
        
        self.__toggle_filter(False)
               

            
    @Slot()
    def __on_text_changed(self):
        """
        Clears the account_table when the text in the
        client_number_edit field changes.

        This ensures irrelevant data is removed before a 
        new search.
        """
        self.account_table.setRowCount(0)
        
  
    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) ->None:
        """
        Opens the Account Details Window for the selected account.

        Connects the balance_updated signal to update the account table
        if any transaction occurs. Displays an error if the selection
        is invalid.
        
        Args:
            row(int): The row index of the selected account in the
            account_table. 
            column (int): The column index of the selected
            cell in the account_table.
        """

        account_number_item = self.account_table.item(row, 0)
        
        account_number = int(account_number_item.text())
        
        if not account_number_item or not account_number_item.text().strip():

            QMessageBox.information(self, "Invalid Selection",
                                    "Please select a valid record.")
        
        account_number = int(account_number_item.text())

        if account_number in self.__accounts:
            selected_account = self.__accounts[account_number]
            account_details_window = AccountDetailsWindow(selected_account)

            account_details_window.balance_updated.connect(self.__update_data)

            account_details_window.exec_()
            
        else:
            QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.")
            

    @Slot(BankAccount)
    def __update_data(self, account: BankAccount):
        """
        Updates the account table and internal account record
        with the latest balance.

        Args:
            account (BankAccount): The updated BankAccount object
            with the latest balance.
        """

        
        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()) == account.account_number:
                self.account_table.item(row, 1).setText(f"${account.balance:.2f}")
                self.__accounts[account.account_number] = account
                update_data(account)  
                break
            
            
    @Slot()
    def __on_filter_clicked(self):
        """
        
        """
        current_text_value = self.filter_button.text()
        if current_text_value == "Apply Filter":
            column_index = self.filter_combo_box.currentIndex()
            filter_edit_text = self.filter_edit.text()
            
            for i in range(self.account_table.rowCount()):
                item = self.account_table.item(i, column_index)
                if item:
                    cell_text = item.text().lower()
                    match = filter_edit_text in cell_text
                    self.account_table.setRowHidden(i, not match)

        # Filtering applied
            self.__toggle_filter(True)

        else:
        # Clear filter: show all rows
            for i in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(i, False)

        # Filter removed
            self.__toggle_filter(False)
    
    
    def __toggle_filter(self, filter_on: bool):
        """
        Toggles the state of filter widgets to indicate whether filtering is applied.
        """
        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            
            for i in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(i, False)

            self.filter_label.setText("Data is Not Currently Filtered")

        
                
                
                
            
        
        
        