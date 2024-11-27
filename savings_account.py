##  """Import the Account class from the Account.py file."""

from Account_Class import Account

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

    # User prompt to set the savings balance and interest rate
    balance = float(input("What is your savings account balance? "))
    interest_rate = float(input("What is the interest rate for the savings account? "))
    months = int(input("Over how many months? "))
    
    print(f"Balance: {balance}, Interest Rate: {interest_rate}")
          
    # Create an instance of the `Account` class and pass in the balance and interest parameters set to 0.
    #  Hint: You need to add the interest as a value, i.e, 0.
    new_account = Account(balance, 0)
    
    # Calculate interest earned
    interest = interest_rate * balance * months
    new_account.interest = interest

    # Update the savings account balance by adding the interest earned
    new_account.balance += interest

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    return(f"Updated Balance: ${new_account.balance}")
#   # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # return(f"Interest Earned: $, {new_account.interest}")

#     # Return the updated balance and interest earned.
#     return('New Balance: $', format(balance, ',.2f'))

