# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s). Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Gaganpreet Kaur

## Assignments:
Assignment - 01: This is module 1 Assignment which is based on classes, encapsulation and unit test planning.

Assignment - 02: This is module 2 Assignment which is based on Abstraction, Inheritance and Polymorphism.

Assignment - 03: This is module 3 Assignment which is based on design patterns such as observer pattern, startegy pattern and exploring their implementation and use cases.

Assignment - 04: This is module 4 Assignment which is based on Programming Paradigms.

Assignment - 05: This is Module 5 Assignment which is based on Algorithms, Help Files and Distribution.


## Encapsulation
[use this section to explain how Encapsulation was achieved in the BankAccount class.]
Encapsulation in the BankAccount class is achieved by private attributes such as __account_number, __balance to protect the sensitive data from direct access. Controlled access is provided by public methods such as deposit() or withdraw(). This approach keeps the data secure, ensures all changes are checked and provide simple methods to use the class.

## Polymorphism
[use this section to explain how Polymorphism was achieved in the BankAccount subclasses.]
Polymorphism in the BankAccount subclasses is achieved by overriding method such as get_service_charges() in each subclass. While the method names and parameters stay the same across all account types, each subclass provides its own implementation to its specific account type. This allows different account types to behave differently when the same method is called, making the program more flexible and dynamic.

## Strategy Pattern
[use this section to explain how the Strategy Pattern is being used in this application.]
The Strategy Pattern is used in this application to calculate service charges dynamically based on distinct conditions. Instead of having a fixed calculation method in the BankAccount class, various strategies like MinimumBalanceStrategy, OverdraftStrategy, and ManagementFeeStrategy implement their own logic for determining service charges. This allows flexibility, making it easy to switch or add new charge calculation methods without modifying the core account functionality.

## Observer Pattern
[use this section to explain how the Observer Pattern is being used in this application.]
The Observer Pattern is used in this assignment by having BankAccount which is acting as a subject that notifies MinimumBalanceStrategy, ManagementFeeStrategy and OverdraftStrategy whenever account details change. This allows the strategy to automatically recalculate service charges, ensuring updates are applied dynamically. This approach improves maintainability and keeps the service charge logic adaptable to changes in account status.

## Event-Driven Programming Paradigm
[use this section to explain how the Event-Driven Programming Paradigm is employed in this application.]
In this assignment, this application follows the Event-Driven Programming Paradigm by responding to user interactions such as button clicks and table cell selections. A pop-up message box appears when invalid input is detected or a transaction fails. The balance is automatically updated when a deposit or withdrawal occurs, using custom signals like balance_updated to reflect changes across windows in real time.