# File Name: school.py
# Date: 11/16/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: Holds the functions for creating a student, finding a student, and creating the default students

class Student:
    def __init__(self, fname: str, lname: str):
        """Constructor function, defines starting attributes"""
        self.first_name = fname
        self.last_name = lname
        self.id_number = 0
        self.total_credits = 0
        self.GPA_points = 0

    def addClass(self, letter_grade: str, credit_worth: int):
        """Adds a class (credits) to the students record"""
        # add credits to students total credit count
        self.total_credits += credit_worth
        
        # get correct points based on letter grade
        points = -1
        if letter_grade.capitalize() == 'A':
            points = 4
        elif letter_grade.capitalize() == 'B':
            points = 3
        elif letter_grade.capitalize() == 'C':
            points = 2
        elif letter_grade.capitalize() == 'D':
            points = 1
        elif letter_grade.capitalize() == 'F':
            points = 0
        
        # calculate gpa point using: points * credits
        class_worth = points * credit_worth
        self.GPA_points += class_worth

    def getGPA(self) -> float:
        """Calculates the students GPA"""
        try:
            GPA = self.GPA_points / self.total_credits
        except:
            GPA = 0
        finally:
            return GPA


def get_class() -> list:
    """Creates 3 default student objects, adds them to a list"""
    def_studs = [['Kohl', 'Johnson', '101'], ['Leonardo', 'DiCaprio', '102'], ['Ryan', 'Reynolds', '103']]
    studs_list = []

    for ndx in range(len(def_studs)):
        first_name = def_studs[ndx][0]
        last_name = def_studs[ndx][1]
        stud = Student(first_name, last_name)
        stud.id_number = def_studs[ndx][2]
        # add to list
        studs_list += [stud]

    return studs_list


def get_roster(list_students: list) -> str:
    """Accepts list of students, returns string in form of a table"""
    table_string = ""
    count_num = 1

    # cycle through list of student objects
    for ndx in range(len(list_students)):
        # get info from student object
        stud_num = count_num
        stud_ident = list_students[ndx].id_number
        stud_name = list_students[ndx].first_name + " " + list_students[ndx].last_name
        stud_credits = list_students[ndx].total_credits
        stud_gpa = list_students[ndx].getGPA()
        
        # concate together
        stud_info = "{:<5}{:<5}{:<20}{:<10}{:<5.2f}\n".format(stud_num, stud_ident, stud_name, stud_credits, stud_gpa)
        
        # add to table string
        table_string += stud_info
        
        # update count num
        count_num += 1

    return table_string


def get_student(list_students: list) -> object:
    """Accepts list of students, searches list by number in list"""
    is_valid = False

    # loop for making sure input is correct
    while not is_valid:
        search_num = int(input("Enter Student Number (num from list): "))
        if search_num > 0 and search_num <= len(list_students):
            is_valid = True
        else:
            is_valid = False
            print("Invalid range, try again.")

    # index for object is offset by 1 becasue num does NOT start at zero, starts at 1
    student_obj = list_students[search_num - 1]
    return student_obj
