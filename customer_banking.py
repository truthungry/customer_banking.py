# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():

    """This function will call upon the savings account and cd account files to create a new account.
       The user will be prompted for the starting balance, interest rate, and the length of months to determine the interest gained.
       It will display the interest earned on the savings and CD accounts, and update the balances.
    """

    # # Call the create_savings_account function, which pass the variables from the user.
create_savings_account()
    # # Call the create_cd_account function and pass the variables from the user.
create_cd_account()

# Call the main function.
if __name__ == "__main__":
    main() 