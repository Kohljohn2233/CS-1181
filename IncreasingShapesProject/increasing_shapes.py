# File Name: increasing_shapes.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 09-09-2021
# Professor: Jon Holmes
# Description: This program will...
# 1. Ask the user how many shapes should be drawn
# 2. Ask the user how many sides those shapes will have
# 3. Calculate the angle needed for each turn by: turn_angle = 360 / number of sides
# 4. Increase the length of each side by 10 for each shape drawn

import turtle  # imports turtle module

# Prompt user for input data
str_shape_count = input("Enter amount of shapes: ")  # prompts user to enter amount of shapes to draw
str_side_count = input("Enter amount of sides: ")  # prompts user to enter amount of sides for each shape

# Change input strings to float data type
shape_count = int(str_shape_count)  # converts str_shape_count from string to float data type
side_count = int(str_side_count)  # converts str_side_count from string to float data type

# Create turtle object and loop variables
shape = turtle.Turtle()  # creates a turtle object with "shape" being the name
shape.color("orange")  # changes the color of the lines to orange
cur_shape = 1  # sets cur_shape number to 1 (for printing stuff)
cur_side = 1  # sets cur_side number to 1 (for printing stuff)
cur_length = 40  # sets the starting length to 40
angle_step = 360 / side_count  # calculates the angle for each turn by 360 / amount of sides

# Outside Loop Start --------------------------------------------------------------------------------------
for cur_shape in range(shape_count):  # start of the shape for loop
    print("Current Shape Number: " + str(cur_shape + 1))  # prints out the number for the current shape being drawn
    # Inside Loop Start ---------------------------------------------------------------------------
    for cur_side in range(side_count):  # start of the sides for each shape loop
        print("    Current Side Number: " + str(cur_side + 1))  # prints out the current side number being drawn
        shape.forward(cur_length)  # tells the turtle object to draw forward by cur_length
        shape.left(angle_step)  # tells the turtle object to turn left by the angle_step
    # Inside Loop End ---------------------------------------------------------------------------
    cur_length += 10  # runs this after the first object is drawn, increases cur_length by 10
    shape.penup()  # lifts the turtle pen up to stop from drawing
    shape.backward(5)  # moved the turtle cursor back by 5 for offsetting the next start point
    shape.pendown()  # puts the turtle pen down to start drawing
# Outside Loop End --------------------------------------------------------------------------------------

print("Done!")  # after all shapes and sides are drawn will print out "done!"
turtle.exitonclick()  # for closing the turtle drawing window
