"""Import the Account class from the Account.py file."""
from Account_Class import Account

# Define a function for the Savings Account
def create_savings_account():
    
# Create an instance of the `Account` class and pass in the balance and interest parameters.
    new_savings_account = Account(interest=0, balance=0, months=0 ,interest_rate=0, new_balance=0)

"""Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
"""

# Prompt the user to set the balance, interest rate, and months for the interest.
balance = float(input("\nEnter the starting savings balance: $"),)
interest_rate = float(input("Enter the interest rate: "),)
months = int(input("Over how many months? "))
    
# Calculate interest earned
interest = balance * interest_rate * months

# Calculate the new balance
new_balance = balance + interest

# Return the new savings balance and the interest earned
print(f'\nStarting Savings balance: $', format(balance, '.2f')'')
print(f'Interest Earned: $', format(interest, ',.2f'),'')
print(f'New Savings balance after {months} months: $', format(new_balance, '.2f'),'')

