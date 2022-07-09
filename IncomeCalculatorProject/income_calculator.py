# File Name: income_calculator.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 09-01-2021
# Professor: Jon Holmes
# Description: This program will..
# 1: Ask the user to input their hourly wage, hours per week, and desired annual pay.
# 2: Calculate the weekly, monthly, and annual pay from the user's current job.
# 3: Calculate the number of hours per week needed to reach the desired annual pay while keeping current hourly wage.
# 4: Calculate the hourly wage needed to reach desired annual pay while keeping current hours per week.
# 5: return all the calculated data back to the user via the print function.

# Ask user to input current job stats
str_cur_weekly_hours = input("Current hours per week: ")  # input weekly hours
str_cur_hourly_wage = input("Current hourly pay: ")  # input hourly wage

# Ask user to input ideal job stats
str_ideal_annual_income = input("Ideal Annual Income: ")  # input ideal annual income

# Convert from strings to float data type
cur_hourly_wage = float(str_cur_hourly_wage)  # change from string to float
cur_weekly_hours = float(str_cur_weekly_hours)  # change from string to float
ideal_annual_income = float(str_ideal_annual_income)  # change from string to float

# Calculations
cur_weekly_income = cur_hourly_wage * cur_weekly_hours  # calculate weekly income by: hourly pay * weekly hours
cur_monthly_income = cur_weekly_income * 4  # calculate monthly pay by: weekly income * 4
cur_yearly_income = cur_weekly_income * 52  # calculate yearly pay by: weekly income * 52

hours_needed_ideal_income = ideal_annual_income / 52 / cur_hourly_wage  # calculate hours needed at current job to reach ideal income
wage_needed_ideal_income = ideal_annual_income / 52 / cur_weekly_hours  # calculate wage needed at current job to reach ideal income

# Return data from calculations
print("At your current job, if you work", str(cur_weekly_hours), "hour(s) per week at $" + format(cur_hourly_wage, ".2f"), "per hour you will...")
print(" Earn $" + format(cur_weekly_income, ".2f"), "per week.")
print(" Earn $" + format(cur_monthly_income, ".2f"), "per month.")
print(" Earn $" + format(cur_yearly_income, ".2f"), "per year.")
print("To reach your ideal yearly income of $" + format(ideal_annual_income, ".2f") + ", you will need to...")
print(" Work " + format(hours_needed_ideal_income, ".2f"), "hours a week at your current hourly rate of $" + format(cur_hourly_wage, ".2f"), "or")
print(" Keep working " + str(cur_weekly_hours), "hours a week but at a new hourly rate of $" + format(wage_needed_ideal_income, ".2f"))
