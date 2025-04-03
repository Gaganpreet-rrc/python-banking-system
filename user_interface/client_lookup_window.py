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
        super().__init__()
        
        self.__client_listing, self.__accounts = load_data()
        
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        
    @Slot()
    def __on_lookup_client(self):
        """
        
        """
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.information(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()
            return
        
        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: {client_number} not found.")
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
                
                account_number_item = QTableWidgetItem(str(account.account_number))
                balance = QTableWidgetItem(f"${account.balance:,.2f}") 
                date_created_item = QTableWidgetItem(account._date_created.strftime("%Y-%m-%d")) 
                account_type_item = QTableWidgetItem(account.__class__.__name__) 
                
                balance.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_number_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)
 
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)
                
        self.account_table.resizeColumnsToContents()
               

            
    @Slot()
    def __on_text_changed(self):
        """
        
        """
        self.account_table.setRowCount(0)
        
  
    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) ->None:
        """
        
        """
        account_number_item = self.account_table.item(row, 0)
        
        account_number = int(account_number_item.text())
        
        if not account_number_item or not account_number_item.text().strip():

            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
        
        account_number = int(account_number_item.text())

        if account_number in self.__accounts:
            selected_account = self.__accounts[account_number]
            account_details_window = AccountDetailsWindow(selected_account)
        
            account_details_window.exec_()
            
        
        else:
            QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.")
            

        
            

            
        
        
        
        
        
        
        
        
        
    
        
        
        
    
        
