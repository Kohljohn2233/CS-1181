# File Name: loan_calculator.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 09-23-2021
# Professor: Jon Holmes
# Description:
# 1. Prompts the user to enter loan amount, loan length in years, and the interest rate
# 2. Runs those values through the functions in the loan_calculator.py file
# 3. Prints out the formatted values in X amount of rows depending on length of loan in months

import loan_calculator
import math


def get_loan_amount() -> float:
    """Accepts nothing as input, but prompts the user to enter their loan amount"""
    str_loan_amount = input("How much money did you borrow? ")
    loan_amount = float(str_loan_amount)
    return loan_amount


def get_loan_length_in_years() -> float:
    """Accepts nothing, but prompts the user to enter their loan length in years"""
    str_loan_length = input("How many years will it take to pay off? ")
    loan_length = float(str_loan_length)
    return loan_length


def get_monthly_rate() -> float:
    """Accepts nothing, prompts the user to enter their interest rate"""
    str_monthly_rate = input("What is your interest rate? ")
    monthly_rate = float(str_monthly_rate)
    return monthly_rate


def get_length_in_months(loan_length_years: float) -> int:
    """Accepts the loan length in years, turns that amount into months"""
    float_loan_length_months = loan_length_years * 12
    loan_length_months = int(float_loan_length_months)
    return loan_length_months


def get_table_row(month: int, loan_amount: float, monthly_payment: float, interest_amount: float, end_balance: float):
    """Accepts the current month, current loan amount, the monthly payment, and end balance then generates the row of values in the table"""
    str_month = str(month)  # turns month variable from int into a string
    str_loan_amount = str(format(loan_amount, ".2f"))  # turns loan amount from float to a string with 2 decimal places
    str_monthly_payment = str(format(monthly_payment, ".2f"))  # turns monthly payment from float to a string with 2 decimal places
    str_interest_amount = str(format(interest_amount, ".2f"))  # turns interest amount from float to a string with 2 decimal places
    str_end_balance = str(format(math.fabs(end_balance), ".2f"))  # turns end balance from float to a string with 2 decimal places

    formatted_loan_amount = str_loan_amount.ljust(10)  # formats the string to be 10 spaces wide (website: https://www.w3schools.com/python/ref_string_ljust.asp)
    formatted_monthly_payment = str_monthly_payment.ljust(10)  # formats the string to be 10 spaces wide
    formatted_interest_amount = str_interest_amount.ljust(10)  # formats the string to be 10 spaces wide
    formatted_end_balance = str_end_balance.ljust(10)  # formats the string to be 10 spaces wide
    print(str_month + "\t\t$" + formatted_loan_amount + "\t\t$" + formatted_interest_amount + "\t\t$" + formatted_monthly_payment + "\t\t$" + formatted_end_balance)


# -- Start Point for Program --
base_loan_amount = get_loan_amount()  # runs the function to get the loan amount
time_period = get_length_in_months(get_loan_length_in_years())  # runs the two functions to get the time period in months
base_interest_rate = get_monthly_rate()  # runs the function to get the interest rate

# Non-Changing Variables
monthly_interest_rate = loan_calculator.monthly_rate(base_interest_rate)  # runs the function to get the monthly interest rate
amount_due_monthly = loan_calculator.monthly_payment(base_loan_amount, time_period, monthly_interest_rate)  # runs the function to get the monthly payment

# Changing Variables
current_loan_amount = base_loan_amount  # sets the current amount owed to the base amount owed
monthly_interest_amount = loan_calculator.monthly_interest(current_loan_amount, monthly_interest_rate)  # runs the function to get the interest amount for the month
total_interest_paid = monthly_interest_amount  # sets the base total interest paid with the calculated first months interest

# print out the header blocks
print("\nMonth\tBalance\t\t\tInterest\t\tPayment\t\t\tEnd Balance")  # prints out the header blocks

# Loop
for current_month in range(1, time_period + 1):

    balance = loan_calculator.end_of_month_balance(current_loan_amount, monthly_interest_amount, amount_due_monthly)  # calculates the end of month balance
    get_table_row(current_month, current_loan_amount, amount_due_monthly, monthly_interest_amount, balance)  # runs the script to print out the row

    current_loan_amount = balance  # updates the current loan amount to be equal to the end of month balance

    monthly_interest_amount = loan_calculator.monthly_interest(current_loan_amount, monthly_interest_rate)  # runs the monthly interest to get the amount of interest due

    total_interest_paid += monthly_interest_amount  # updates total interest paid by adding the monthly interest amount

# End Loop
print("\nDone generating loan amortization table.")
print("\n-- Extra Information --")
print("Total Interest Paid: $" + str(format(total_interest_paid, ".2f")))
print("Actual Loan Cost: $" + str(format(base_loan_amount + total_interest_paid, ".2f")))
