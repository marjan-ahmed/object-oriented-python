Bank Account System — Project Task List
=======================================

Project Overview
----------------

Build a simple bank account management system using Object-Oriented Programming (OOP) principles in Python.The system should allow users to create accounts, deposit and withdraw money, track transactions, and display balances.

Tasks
-----

### 1\. **Define BankAccount Class**

*   Create a class named BankAccount.
    
*   Add the following attributes:
    
    *   account\_number (int)
        
    *   account\_holder (str)
        
    *   \_\_balance (private float/int, initial balance)
        
    *   transaction\_count (int, starts at 0)
        

### 2\. **Implement Constructor (\_\_init\_\_)**

*   Initialize the attributes with values passed during object creation.
    

### 3\. **Create Getter for Balance**

*   Add a @property method called balance to return the current balance.
    
*   Make sure the balance attribute is private and not directly accessible.
    

### 4\. **Implement Deposit Method**

*   Define a method deposit(amount) to add money to the account.
    
*   Validate that the deposit amount is positive.
    
*   Update the balance and increase the transaction count.
    
*   Return the updated balance.
    

### 5\. **Implement Withdraw (Credit) Method**

*   Define a method withdraw(amount) to withdraw money from the account.
    
*   Validate that the amount is positive and does not exceed the current balance.
    
*   Deduct the amount from the balance and increase the transaction count.
    
*   Return the updated balance.
    

### 6\. **Implement Transaction Tracking**

*   Add a counter that tracks the number of transactions (deposits + withdrawals).
    

### 7\. **Implement a Method to Check Balance**

*   Add a method check\_balance() that returns a formatted string with account holder's name and current balance.
    

### 8\. **Add Transaction Timestamp (Optional / Advanced)**

*   Implement a decorator that prints the date and time whenever a deposit or withdrawal occurs.
    

### 9\. **Create a Derived Class: SavingAccount**

*   Inherit from BankAccount.
    
*   Add a method add\_interest(rate) that calculates and adds interest to the balance.
    
*   Override check\_balance method if necessary for customized output.
    

### 10\. **Test Your Classes**

*   Create instances of BankAccount and SavingAccount.
    
*   Test deposits, withdrawals, interest addition, and balance checks.
    
*   Verify transaction count increments properly.
    
*   Check error handling on invalid operations.
    

Bonus Tasks (Optional)
----------------------

*   Implement input validation with exception handling.
    
*   Save transaction history with timestamps.
    
*   Add support for multiple accounts stored in a collection.
    
*   Create a command-line interface (CLI) for users to interact with the system.
    
*   Implement persistence using file or database storage.
    

How to Run
----------

*   Write test cases or interactive prompts in your main script.
    
*   Create instances and call methods to see results.
    
*   Use print statements or logging to display outputs.
    

Example Expected Output
-----------------------

YAML

```
You deposited at 2025-05-19 17:04:46.275900
200
User Marjan balance is 200
You credited at 2025-05-19 17:04:46.277609
90
User Marjan balance is 110
Transaction history: 2
```