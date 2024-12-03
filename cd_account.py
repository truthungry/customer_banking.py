"""Import the Account class from the Account.py file."""
from Account_Class import Account

# Define a function for the CD Account
def create_cd_account():

# Create an instance of the `Account` class and pass in the balance and interest parameters.
    new_cd_account = Account(interest_rate=0, balance=0, months=0, interest=0, new_balance=0)

"""Creates a CD account, calculates interest earned, and updates the account balance.

        Args:
            balance (float): The initial CD account balance.
            interest_rate (float): The APR interest rate for the CD account.
            months (int): The length of months for the CD.

        Returns:
            float: The updated CD account balance after adding the interest earned.
            And returns the interest earned.
"""

# Prompt the user to set the balance, interest rate, and months for the interest.
balance = float(input("\nEnter the starting CD balance: $"),)
interest_rate = float(input("Enter the interest rate: "),)
months = int(input("Enter the months of the CD: "))

# Calculate interest earned
interest = balance * interest_rate * months

# Calculate the new balance
new_balance = balance + interest
    
# Return the updated balance and the interest earned
print(f'\nStarting CD balance: $', format(balance, ',.2f'),'')
print(f'Interest Earned: $', format(interest, ',.2f'),'')
print(f'New CD Balance after {months} months: $', format(new_balance, '.2f'),'')