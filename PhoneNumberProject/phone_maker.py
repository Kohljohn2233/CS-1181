# File Name: phone_maker.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 09-16-2021
# Professor: Jon Holmes
# Description:
#   1. Create function called get_number_to_generate
#   2. Create function called get_line_number
#   3. Create function called get_area_code
#   4. Create function called get_office_code
#   5. Print out the number with format: (###) ###-####
#   6. Run all the above functions X amount of times depending on input

import random

# get_number_to_generate function
def get_number_to_generate():
    """Ask user to enter in how many numbers they need"""
    user_input = input("Enter amount of phone numbers to generate: ")  # prompts the user to enter amount of phone numbers to generate
    return user_input  # returns user_input back to the "main" code


# get_line_number function
def get_line_number():
    """Generate the last four digits in the phone number"""
    int_first_number = random.randrange(1, 9)  # first number is between 1 and 9 (inclusive)
    int_last_three = random.randrange(100, 1000)  # last three numbers are between 100 and 999 (inclusive)
    str_first_number = str(int_first_number)  # changes the data type from integer to string
    str_last_three = str(int_last_three)  # changes the data type from integer to string
    str_line_number = str_first_number + str_last_three  # combines the two strings together to from the line number
    return str_line_number  # returns str_line_number back to the "main" code


# get_area_code function
def get_area_code(int_first_number):
    """Generates the 3 numbers for the area code"""
    int_second_number = random.randrange(0, 2)  # random number either 0 or 1 (inclusive)
    int_third_number = random.randrange(1, 10)  # random number between 1 and 9 (inclusive)
    str_first_number = str(int_first_number)  # changes the data type from integer to string
    str_second_number = str(int_second_number)  # changes the data type from integer to string
    str_third_number = str(int_third_number)  # changes the data type from integer to string
    str_area_code = str_first_number + str_second_number + str_third_number  # combines the three seperate strings to from the area code
    return str_area_code  # returns str_area_code back to the "main" code


# get_office_code function
def get_office_code(int_first_number):
    """Generates the 3 digits for the office code"""
    int_second_number = random.randrange(2, 10)  # random number between 2 and 9 (inclusive)
    int_third_number = random.randrange(1, 10)  # random number between 1 and 9 (inclusive)
    str_first_number = str(int_first_number)  # changes the data type from integer to string
    str_second_number = str(int_second_number)  # changes the data type from integer to string
    str_third_number = str(int_third_number)  # changes the data type from integer to string
    str_office_code = str_first_number + str_second_number + str_third_number  # combines the 3 strings together to from the office code
    return str_office_code  # returns str_office_code back to the "main" code


# Start point for the phone number generator
str_run_amount = get_number_to_generate()  # calls the get_number_to_generate function to run, does not put any input (arguments) into it
int_run_amount = int(str_run_amount)  # changes the input string into an integer data type for use with the "for" loop
int_current_number = 1  # used as eye candy to keep track of which phone number is currently being generated

# For loop to generate phone numbers X amount of times
for int_run_amount in range(int_run_amount):
    str_area_code = get_area_code(random.randrange(2, 10))  # chooses a random number between 2 and 9 and inputs that number into the get_area_code function
    str_office_code = get_office_code(random.randrange(2, 10))  # choose a random number between 2 and 9 and inputs that number into the get_office_code function
    str_line_number = get_line_number()  # calls the get_line_number function to be run but does not input any arguments
    print("\nNumber " + str(int_current_number))  # eye candy
    print("    Area Code:   " + str_area_code)  # prints out the area code separate (mainly for testing)
    print("    Office Code: " + str_office_code)  # prints out the office code separate (mainly for testing)
    print("    Line Number: " + str_line_number)  # prints out the line number separate (mainly for testing)
    print("    Formatted:   (" + str_area_code + ") " + str_office_code + "-" + str_line_number)  # prints out the full phone number formatted correctly
    int_current_number += 1  # increases the int_current_number variable by one to keep track of the current phone number count


print("\nDone generating " + str_run_amount + " phone numbers!")  # when done with the "for" loop will print out the statement meaning the generator is done
