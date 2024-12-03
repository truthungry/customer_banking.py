#""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance=0, months=0, interest=0, new_balance=0, interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = interest
        self.months = months
        self.new_balance = new_balance

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the account"""
        return balance.self
    
    # This method sets the interest rate for the account.
    def set_interest_rate(self, interest_rate):
        """Sets the interest rate for the account"""
        interest_rate = self.interest_rate / 100    
        return interest_rate.self
    
    # This method sets the months for the account
    def set_months(self, months):
        return months.self

    # # The method sets the interest gained for the savings account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        return interest.self

    # Calculate interest earned on the account
    def calculate_interest_earned(self, interest, balance, months, interest_rate):
        interest_rate = self.interest_rate / 100
        interest = balance * interest_rate * months
        return interest.self

    #  Returns new balance with interest earned
    def new_balance(balance, interest):
        new_balance = balance + interest
        return new_balance.self
