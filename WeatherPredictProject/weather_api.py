# File Name: weather_api.py
# Course: CS 1181
# Name: Kohl Johnson
# Date: 10-3-2021
# Professor: Jon Holmes
# Description:
#   1. number_is_in_range function is used to make sure the number the user inputs is between 1 and 10
#   2. get_temperature function generates a random float number between a given range depending on the city
#   3. temperature_description function gives a temp description depending on the temperature
#   4. get_weather function generates a random weather type 50% chance of sunny, 25% partly cloudy, 25% precipitation

import random


def number_is_in_range(predict_count: int, min_count: int, max_count: int) -> int:
    """Checks the inputted number of predictions against the min and max value"""
    if (predict_count < min_count) or (predict_count > max_count):
        print("\nInvalid input for the number of predictions, defaulting to 8.")
        predict_bool = False
    else:
        predict_bool = True

    return predict_bool


def get_temperature(name_of_city: str) -> float:
    """Returns a random temperature within limits for the correct city"""
    if name_of_city == "Pocatello":
        ran_temp = random.uniform(16.0, 87.9)
    elif name_of_city == "Orlando":
        ran_temp = random.uniform(50.0, 91.9)
    elif name_of_city == "Salt Lake City":
        ran_temp = random.uniform(26.0, 89.9)
    elif name_of_city == "Dallas":
        ran_temp = random.uniform(30.0, 94.9)
    elif name_of_city == "Ann Harbor":
        ran_temp = random.uniform(18.0, 82.9)
    elif name_of_city == "Phoenix":
        ran_temp = random.uniform(46.0, 105.9)
    elif name_of_city == "Anchorage":
        ran_temp = random.uniform(11.0, 64.9)
    elif name_of_city == "Honolulu":
        ran_temp = random.uniform(66.0, 87.9)
    else:
        ran_temp = 0

    return ran_temp


def temperature_description(temp: float) -> str:
    """Returns the temperature description from the input temp"""
    if temp <= 32:
        temp_description = "COLD"
    elif (temp > 32) and (temp <= 50):
        temp_description = "COOL"
    elif (temp > 50) and (temp <= 70):
        temp_description = "MILD"
    elif (temp > 70) and (temp <= 85):
        temp_description = "WARM"
    elif temp > 85:
        temp_description = "HOT"

    return temp_description


def get_weather(temp: float) -> str:
    """Gets a weather prediction"""
    chance = random.randrange(1, 101)

    if chance <= 50:
        weather_description = "sunny"
    elif (chance > 50) and (chance <= 75):
        weather_description = "partly cloudy"
    elif chance > 75:
        weather_description = "precipitation"
        if (weather_description == "precipitation") and (temp < 32):
            weather_description = "snowy"
        else:
            weather_description = "rainy"

    return weather_description
