# File Name: package_calculations.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 10-7-2021
# Professor: Jon Holmes
# Description:

import package_calculations
# welcome message
print("Welcome to the shipping department. To use our system, you will..")
print(" [1] be asked if you want to add a load, this answer must be either Y or N.")
print(" [2] be asked the weight of that load, this amount must be entered in pounds.")
print("Once all the loads are entered, the system will calculate the following data:")
print(" - Load Number")
print(" - Pound Weight")
print(" - KG Weight")
print(" - Total Weight")
print("Note: due to processing time, any shipment exceeding a total weight of 500kg will be sent immediately, without the option to add another load.")
print("The program will then print out the above data on a table and also the amount of 20kg packing boxes required.\n")


# program start variables
loop_bool = True
load_counter = 0
total_load_weight = 0
total_box_count = 0
formatted_row = ""

while loop_bool and total_load_weight <= 500:
    # ask if user wants to enter another load
    loop_bool = package_calculations.get_another_load()

    if loop_bool:  # if loop_bool = True
        # increase counter
        load_counter += 1
        # ask for load weight
        pound_load_weight = package_calculations.get_weight(load_counter)
        # convert to kg
        load_weight = package_calculations.convert_to_kg(pound_load_weight)
        # add to total load weight
        total_load_weight += load_weight
        # send data to package_calculations.py for turning into string to store
        formatted_row += package_calculations.format_output_row(load_counter, pound_load_weight, load_weight, total_load_weight)

# check to make sure data was actually entered, if not print alternate end message
if total_load_weight > 0:
    # skip a couple lines
    print("\n\n")
    # print out separation line
    print("----------------------------------------------------------------")
    # print out header block
    print("Load\t\t\tPounds\t\t\tKilograms\t\tTotal Kilograms")
    # print out data string
    print(formatted_row)
    # print out separation line
    print("----------------------------------------------------------------")
    # print out total shipment weight
    print("\t\t\t\t\t\t Total Shipment Weight: " + str(format(total_load_weight, ".3f")) + " kg\n")
    # print out the required amount of boxes
    total_box_count = package_calculations.number_of_boxes_needed(total_load_weight)
    print("In order to ship " + str(load_counter) + " load(s), we need " + str(total_box_count) + " boxes.")
    # print out end message
    print("\n-- End of Program -- \nThank you for using the shipping department!")
else:
    print("\nNo data entered to print to table.\nEnd of program.")
