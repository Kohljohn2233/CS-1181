# File Name: course_data.py
# Date: 11/16/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: Front page of the program, contains the menu loop 

import school

def add_new_student(list_students: list) -> list:
    """Custom function to add a new student"""
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    new_student = school.Student(first_name.strip(), last_name.strip())

    # check to make sure its 3 digits
    is_valid_id = False
    is_id_three = False
    is_id_taken = True
    while not is_valid_id:
        new_stud_id = input("Enter New ID Number (3 digits): ")

        # check to make sure its 3 digits
        if len(new_stud_id) != 3:
            print("Student ID must be 3 digits. No more, No less.\n")
            is_id_three = False
        else:
            is_id_three = True

        # check to make sure its not already taken
        if is_id_three:
            is_id_taken = False
            for ndx in range(len(list_students)):
                stud = list_students[ndx]
                enrolled_stud_id = stud.id_number

                if new_stud_id == enrolled_stud_id:
                    print("ID matches with already enrolled student, please enter a new one.\n")
                    is_id_taken = True

        # check if both above 'checks' are valid
        if is_id_three and not is_id_taken:
            is_valid_id = True
        else:
            is_valid_id = False

         
    # add id to newly created student
    new_student.id_number = new_stud_id

    # append student list
    list_students.append(new_student)

    # return updated list
    return list_students


def add_student_grade(list_students: list):
    """Custom function to update student grades"""
    student_object = school.get_student(list_students)

    # valid letter grade checking
    valid_letter_grade = False
    while not valid_letter_grade:
        letter_grade = input("Enter Letter Grade (A B C D F): ")
        if letter_grade.capitalize() == 'A' or letter_grade.capitalize() == 'B' or letter_grade.capitalize() == 'C' or letter_grade.capitalize() == 'D' or letter_grade.capitalize() == 'F':
            valid_letter_grade = True
        else:
            print("Invalid input, try again.\n")
            valid_letter_grade = False

    # valid credit worth checking
    valid_credit_worth = False
    while not valid_credit_worth:
        str_credit_worth = input("Enter Credit Worth: ")
        try:
            credit_worth = int(str_credit_worth)
            if credit_worth >= 0:
                valid_credit_worth = True
            else:
                valid_credit_worth = False
                print("Invalid input, try again.\n")
        except:
            print("Invalid input, try again.\n")
            valid_credit_worth = False
    
    # update student attributes
    student_object.addClass(letter_grade, credit_worth)


# welcome message, menu string, and table header string
print("Welcome to the student registrar! Please follow the menu options below.")
menu = "------ Menu Options ------\n1. List All Students   - l\n2. Add New Student     - a\n3. Enter Student Grade - e\n4. Exit Application    - x\n"
header = "{:<5}{:<5}{:<20}{:<10}{:<5}".format("Num", "ID", "Name", "Credits", "GPA")
top_spacer = '=' * 45
bottom_spacer = '-' * 45

# starting students
student_list = school.get_class()

# program loop
run_program = True
while run_program:
    print("\n" + menu)

    # valid menu choice loop
    is_valid = False
    while not is_valid:
        menu_choice = input("Enter menu choice: ")
        if menu_choice.lower() == "l":
            # list all students
            print(top_spacer)
            print(header)
            print(top_spacer)
            table = school.get_roster(student_list)
            print(table)
            print(top_spacer)
            is_valid = True

        elif menu_choice.lower() == "a":
            # add a new student
            student_list = add_new_student(student_list)
            is_valid = True

        elif menu_choice.lower() == "e":
            # search for student and enter grade
            add_student_grade(student_list)
            is_valid = True

        elif menu_choice.lower() == "x":
            # exit the program
            run_program = False
            is_valid = True
            print("\nThank you for using the registrar office.\n")

        else:
            print("Invalid choice, try again.\n")
            is_valid = False

