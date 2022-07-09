# File Name: package_calculations.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 10-7-2021
# Professor: Jon Holmes
# Description:

import math

# starting variables
load_count = 0


def convert_to_kg(pounds: float) -> float:
    """Converts from pounds to kilograms"""
    # Formula: kg = pounds / 2.205
    kg = pounds / 2.205
    return kg


def number_of_boxes_needed(kg_weight: float) -> int:
    """Calculates the number of boxes needed"""
    # max weight per box = 20kg
    load_num_boxes = math.ceil(kg_weight / 20)
    return load_num_boxes


def get_weight(load_counter: int) -> float:
    """Prompts the user to enter weight in pounds, checks if its within range"""
    weight_input = 0

    while weight_input <= 0 or weight_input > 1000 or type(weight_input) != float:
        # ask for weight
        weight_input = float(input("Enter weight of load " + str(load_counter) + " (in pounds): "))
        # input validation
        if weight_input <= 0:
            # if input less than equal to zero
            print("Invalid input, weight must be greater than zero.\n")
        elif weight_input > 1000:
            # if input greater than 1000
            print("Invalid input, weight can be no more than 1000 pounds.\n")
        else:
            # input within range
            print("Input for load " + str(load_counter) + " passed validation. :)\n")
    return weight_input


def get_another_load() -> bool:
    """Returns a bool indicating if the user wants to enter another load"""
    yes_no_input = "y"
    return_bool = True
    value_inputed = False

    while not value_inputed:
        # ask for y or n
        yes_no_input = input("Would you like to enter another load (y or n)? ")
        # input validation
        if yes_no_input == "y" or yes_no_input == "Y":
            value_inputed = True
            return_bool = True
        elif yes_no_input == "n" or yes_no_input == "N":
            value_inputed = True
            return_bool = False
        else:
            print("Invalid input, answer must be Y or N. Try again.. :/\n")
            value_inputed = False
            return_bool = True

    return return_bool


def format_output_row(load_number: int, weight_pounds: float, weight_kg: float, total_weight: float) -> str:
    """Formats the row into one string with correct spacing, then returns that string"""
    # convert data to string, formatting with correct decimal places
    str_load_number = str(load_number)
    str_weight_pounds = str(format(weight_pounds, ".3f"))
    str_weight_kg = str(format(weight_kg, ".3f"))
    str_total_weight = str(format(total_weight, ".3f"))
    # change the width of string to a formatted width of 15 characters long (don't know why I chose 15 haha)
    form_load_number = str_load_number.ljust(15)
    form_weight_pounds = str_weight_pounds.ljust(15)
    form_weight_kg = str_weight_kg.ljust(15)
    form_total_weight = str_total_weight.ljust(15)
    # put it all together
    output_row = form_load_number + "\t" + form_weight_pounds + "\t" + form_weight_kg + "\t" + form_total_weight + "\n"
    # return the output row
    return output_row
