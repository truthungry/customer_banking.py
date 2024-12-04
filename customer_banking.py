# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
# Prompt the user to set the savings balance, interest rate, and months for the savings account.
balance = float(input('\n''Please enter your savings account starting balance: $'),)
interest_rate = float(input('What is the interest rate (APY) for the savings account? '),)
months = int(input("Over how many months? "))
        
# Call the create_savings_account function and pass the variables from the user.
savings_account, new_balance, interest_earned = create_savings_account(balance, interest_rate, months)

# Print out the interest earned and updated savings account balance with interest earned for the given months.
print(f"\nUpdated Savings Balance: ${new_balance:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}\n") 

# Prompt the user to set the CD balance, interest rate, and months for the CD account.
#   User prompt to set the savings balance and interest rate.
balance = float(input('Please enter your CD account starting balance? $'))
interest_rate = float(input('What is the interest rate (APY) for your CD account? '))
months = int(input("Over how many months? "))

# Call the create_cd_account function and pass the variables from the user.
cd_account, new_balance, interest_earned = create_cd_account(balance, interest_rate, months)

# Print out the interest earned and updated CD account balance with interest earned for the given months.
print(f"\nUpdated CD Balance: ${new_balance:.2f}")
print(f"Interest Earned: ${interest_earned:.2f} \n") 

# Call the main function.
if __name__ == "__main__":
    main()