### Customer Banking

This project is a customer banking system that allows users to calculate and track the interest earned on savings and CD accounts. 
By running this application, users will be able to enter their savings and CD account balance, interest rate and the number of months to see the interest earned.
Their updated balances is printed, as well as the amount of interest earned. 

In the savings_account.py file, the Account class is imported and the create_savings_account function will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the cd_account.py file, the Account class is imported and the create_cd_account function will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the primary customer_banking.py file, the create_savings_account function is imported from savings_account and the create_cd_account function is imported from cd_account. 
The main function calls each function, which prompts the user to enter the savings and CD account details, calculates the interest earned and update the balance. 
The results for each account as displayed accordingly.