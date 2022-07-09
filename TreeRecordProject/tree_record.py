# File Name: tree_record.py
# Date: 11/28/2021
# Class: CS 1181
# Name: Kohl Johnson
# Professor: Jon Holmes
# Description: Front page of the program, contains the menu loop and functions for adding trees


import trees


def add_pine_tree() -> object:
    """Custom function to add pine tree"""
    new_tree_variety = input("Enter variety: ")  # prompt for variety
    new_tree_needles = int(input("Enter number of needles: "))  # prompt for needles, convert to int
    new_tree_height = int(input("Enter Height (ft): "))  # prompt for height, convert to int
    new_tree_object = trees.Pine(new_tree_variety, new_tree_needles)  # create object
    new_tree_object.height = new_tree_height  # set the height to the new object
    return new_tree_object  # return new tree object


def add_white_pine_tree() -> object:
    """Custom function to add white pine tree"""
    new_tree_height = int(input("Enter Height (ft): "))  # prompt for height, convert to int
    new_tree_object = trees.WhitePine()  # create new tree object
    new_tree_object.height = new_tree_height  # assign the height
    return new_tree_object  # return new tree object


def add_fir_tree() -> object:
    """Custom function for adding fir tree"""
    new_tree_variety = input("Enter Variety: ")  # prompt for variety
    new_tree_height = int(input("Enter Height (ft): "))  # prompt for height, convert to int
    new_tree_object = trees.Fir(new_tree_variety)  # create new tree object
    new_tree_object.height = new_tree_height  # assign height
    return new_tree_object  # return new tree object


def add_aspen_tree() -> object:
    """Custom function for adding aspen tree"""
    new_tree_variety = input("Enter Variety: ")  # prompt for variety
    new_tree_height = int(input("Enter Height (ft): "))  # prompt for height, convert to int
    new_tree_object = trees.Aspen(new_tree_variety)  # create tree object
    new_tree_object.height = new_tree_height  # assign the height
    return new_tree_object  # return the new tree object


def add_generic_tree() -> object:
    """Custom function for adding generic tree"""
    new_tree_type = input("Enter Tree Type: ")  # prompt for type
    new_tree_variety = input("Enter Variety: ") # prompt for variety
    new_tree_height = input("Enter Height (ft): ")  # prompt for height
    new_tree_object = trees.Tree(new_tree_type, new_tree_variety)  # create tree object
    new_tree_object.height = new_tree_height  # assign the height
    return new_tree_object  # return the new tree object


def add_new_tree(tree_object_list: list) -> list:
    """Custom function for adding a new tree"""
    tree_menu = "--- Tree Choices ---\n" \
                "I.   pine -------  p\n" \
                "II.  white pine -  w\n" \
                "III. fir --------  f\n" \
                "IV.  aspen ------  a\n" \
                "V.   diff type --  d\n" \
                "VI.  go back ----  n\n"
    print(tree_menu)

    tree_option_valid = False
    while not tree_option_valid:
        tree_option = input("Enter Choice: ")
        if tree_option == "p":
            new_tree = add_pine_tree()
            tree_object_list.append(new_tree)
            tree_option_valid = True

        elif tree_option == "w":
            new_tree = add_white_pine_tree()
            tree_object_list.append(new_tree)
            tree_option_valid = True

        elif tree_option == "f":
            new_tree = add_fir_tree()
            tree_object_list.append(new_tree)
            tree_option_valid = True

        elif tree_option == "a":
            new_tree = add_aspen_tree()
            tree_object_list.append(new_tree)
            tree_option_valid = True

        elif tree_option == "d":
            new_tree = add_generic_tree()
            tree_object_list.append(new_tree)
            tree_option_valid = True

        elif tree_option == "n":
            tree_option_valid = True

        else:
            print("Invalid choice, try again.\n")
            tree_option_valid = False
    return tree_object_list


def list_all_trees(tree_list: list):
    """custom function to list all trees"""
    table_header = "{:<5}{:<10}{:<20}{:<10}{:<10}".format("Num", "Type", "Variety", "Height", "Clusters")
    thick_spacer = "=" * 55

    print("\n\n" + thick_spacer)
    print(table_header)
    print(thick_spacer)

    data_string = ""
    num = 1
    for tree in tree_list:
        tree_data = "{:<5}{}".format(str(num), tree.getDescription())
        data_string += tree_data
        num += 1
    print(data_string)
    print(thick_spacer)


main_menu = "----- Menu Options -----\n" \
            "I.   add a new tree -- a\n" \
            "II.  list all trees -- l\n" \
            "III. exit program ---- e\n"

print("Welcome to the tree record! Follow the menu choices below.\n")
list_of_trees = trees.get_starting_records()


run_program = True
while run_program:
    print("\n" + main_menu)

    menu_choice_valid = False
    while not menu_choice_valid:
        menu_choice = input("Enter Choice: ")
        if menu_choice == "a":
            list_of_trees = add_new_tree(list_of_trees)
            menu_choice_valid = True

        elif menu_choice == "l":
            list_all_trees(list_of_trees)
            menu_choice_valid = True

        elif menu_choice == "e":
            menu_choice_valid = True
            run_program = False

        else:
            print("Invalid choice, try again.")
            menu_choice_valid = False


print("\nThank you for using the tree record!")
