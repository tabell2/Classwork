# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Tyler Abell
# Section: ENGR-102:538,560
# Assignment: LAB 4b
# Date: 21 sep 2025

import math
from math import *

#Assume a machine during its initial testing phase produces 10 gadgets a day.
# After 10 days of testing (starting on day 11), it begins to ramp up,
# producing 1 more gadget per day (11 gadgets on day 11, 12 on day 12, etc).
# On day 50 it reaches full speed, where it continues to run until on day 101
# it stops producing gadgets.
#reads in a day (as a number) from the keyboard and reports the total number of gadgets
# produced from the initial testing phase up to and including the day entered.

num_days = int(input("Please enter a positive value for day:"))

if num_days < 0:
    print("You entered an invalid number!")
elif num_days <= 10:
    gadgets_made = num_days * 10
elif 10< num_days < 50:
    gadgets_made =
elif  num_days >= 50:
    gadgets_made =

print("The sum total number of gadgets produced on", num_days, "is", gadgets_made)
