"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the CD Account
def create_cd_account(balance, interest_rate, months):

    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    cd_account = Account(balance=0, interest=0)

    # Set balance and interest rate using Account methods
    cd_account.set_balance(balance)
    cd_account.set_interest(interest_rate)
    
    # Calculate interest earned and returns the interest
    interest_earned = balance * (interest_rate / 100 * months/12)

    # Update the CD account balance by adding the interest earned
    new_balance = balance + interest_earned
    cd_account.set_balance(new_balance)  

        # Return the updated balance and interest earned.
    return cd_account, new_balance, interest_earned