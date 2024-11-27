"""Import the Account class from the Account.py file."""
from Account_Class import Account

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
    # User prompt to set the savings balance and interest rate
    balance = float(input("What is your savings account balance? "))
    interest_rate = float(input("What is the interest rate for the savings account? "))
    months = int(input("Over how many months? "))
    
    # print(f"Balance: {balance}, Interest Rate: {interest_rate}")


    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    new_cd_account = Account(balance, 0)

    # Calculate interest earned
    interest = interest_rate * balance * months
    new_cd_account.interest = interest

    # Update the CD account balance by adding the interest earned
    updated_balance = new_cd_account.balance = interest
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    create_cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    create_cd_account.set_interest(interest)

    # Return the updated balance and interest earned.
    return create_cd_account
