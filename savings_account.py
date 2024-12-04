"""Import the Account class from the Account.py file."""
from Account import Account                                                                             

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):

    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(balance, interest=0)
        
    # Set balance and interest rate using Account methods
    savings_account.set_balance(balance)
    savings_account.set_interest(interest_rate)

    # Calculate interest earned and returns the interest
    interest_earned = balance * (interest_rate / 100 * months/12)

    # Update the CD account balance by adding the interest earned
    new_balance = balance + interest_earned    
    savings_account.set_balance(new_balance)

        # Return the updated balance and interest earned.
    return savings_account, new_balance, interest_earned