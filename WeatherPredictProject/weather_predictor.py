# File Name: weather_predictor.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 10-3-2021
# Professor: Jon Holmes
# Description:
#   1. Will ask the user to input the city and the number of predictions they would like
#   2. Will then run the number_is_in_range function from weather_api.py to make sure number of predicions is within range
#   3. Will then go through a loop to generate predictions using the functions from weather_api.py, and print out the values
#   4. Once done with the loop, it will pass the sum of temps to get_average_temp function which will return the average
#   5. Will print out the average amount after

import weather_api  # imports weather_api.py script


def get_average_temp(sum_of_temps: float, num_of_predictions: int) -> float:
    """Calculates the average temperature"""
    average = sum_of_temps / num_of_predictions  # calculates the average
    return average  # returns the average


str_city = input("What city do you want? ")  # prompts the user to enter a city
str_num_predict = input("How many predictions do you want to see (1-10)? ")  # prompts the user to enter number of predictions
num_predict = int(str_num_predict)  # changes he str_num_predict from string to int
temp_sum = 0  # used to hold the sum, starts at 0

# check to make sure entered num predictions falls in correct range
num_check_bool = weather_api.number_is_in_range(num_predict, 1, 10)  # runs the function from weather_api.py, returns a bool
if num_check_bool == False:
    num_predict = 8  # if false it will default the number of predictions to 8
else:
    num_predict = num_predict  # if true no changes will be made to num_predict

# loop for getting X number of predictions
print("------------------------------------------------------------------")
for num_predict in range(1, num_predict + 1):
    temp = weather_api.get_temperature(str_city)  # gets a temp from the function get_temperature by passing the city name
    temp_description = weather_api.temperature_description(temp)  # gets a description of the temp by passing the temp through
    weather = weather_api.get_weather(temp)  # gets the weather by passing in the temp
    print(str(num_predict) + "\t" + "Temperature: " + str(format(temp, ".1f")) + " F" + "\t\t" + "** " + temp_description.ljust(5) + "**" + "\t\t" + "Weather: " + weather)
    temp_sum += temp  # adds the temp to the sum of temps

temp_average = get_average_temp(temp_sum, num_predict)  # gets the average temp by passing in the sum of temps and num of predictions
aver_temp_descrip = weather_api.temperature_description(temp_average)  # gets the temp description of the average temp
print("------------------------------------------------------------------")
print("\nThe average temperature for " + str_city + " was: " + str(format(temp_average, ".1f")) + " F, which is " + aver_temp_descrip + ".")  # prints out the average temp and description
