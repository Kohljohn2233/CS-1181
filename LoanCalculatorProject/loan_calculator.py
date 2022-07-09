# File Name: loan_calculator.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 09-23-2021
# Professor: Jon Holmes
# Description:
# 1. Calculates the monthly rate from the interest rate
# 2. Calculates the monthly interest amount from the current loan amount, and the monthly interest rate
# 3. Calculates the monthly payment from the total loan amount, the length of the loan, and the monthly interest rate
# 4. Calculates the balance at the end of the month from the total loan amount, the monthly interest amount, and the monthly payment

def monthly_rate(base_interest_rate: float) -> float:
    """Calculates the monthly interest rate and returns the value"""
    monthly_interest_rate = (base_interest_rate / 100) / 12  # Equation: (interest_rate / 100) / 12
    return monthly_interest_rate  # returns the monthly_interest_rate


def monthly_interest(current_loan_amount: float, monthly_interest_rate: float) -> float:
    """Calculates the monthly interest amount and returns the value"""
    monthly_interest_amount = current_loan_amount * monthly_interest_rate  # Equation: current_amount * monthly_interest_rate
    return monthly_interest_amount  # returns the monthly amount of interest


def monthly_payment(base_loan_amount: float, time_period: int, monthly_interest_rate: float) -> float:
    """Calculates the monthly payment and returns the value"""
    numerator = monthly_interest_rate * ((1 + monthly_interest_rate) ** time_period)  # Equation: monthly_interest_rate * (1 + monthly_interest_rate)^time_period
    denominator = ((1 + monthly_interest_rate) ** time_period) - 1  # Equation: (1 + monthly_interest_rate)^time_period - 1
    amount_due_monthly = base_loan_amount * (numerator / denominator)  # Equation: amount * (numerator / denominator)
    return amount_due_monthly  # returns the monthly payment due


def end_of_month_balance(current_loan_amount: float, monthly_interest_amount: float, amount_due_monthly: float) -> float:
    """Calculates the end of the month balance and returns the value"""
    balance = current_loan_amount + monthly_interest_amount - amount_due_monthly
    return balance  # returns the balance after interest and the monthly payment is applied
