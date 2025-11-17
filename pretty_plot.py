# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Tyler Abell
# Section: ENGR-102:538,560
# Assignment: LAB 12b
# Date: 17 Nov 2025

import numpy as np
import matplotlib.pyplot as plt

#Create a program named pretty_plot.py that repeatedly multiplies a matrix by a point and plots the
#results.
#Start with a 2D point, (𝑥,𝑦). This point can be represented as a vector: 𝑣 = [𝑥 𝑦 ]. There is also
#defined a 2x2 matrix, 𝑀 = [𝑎 𝑏 𝑐 𝑑 ]. Computing the product of 𝑀 with 𝑣 will give a new point 𝑣′
#: 𝑣′ = 𝑀𝑣. Then, multiply the matrix 𝑀 by the new point 𝑣′, to get another point, i.e. 𝑣′′ = 𝑀𝑣′ .
#This can go on indefinitely, creating a long sequence of points.
#Your program should use numpy to create a matrix and a point. Begin with the point (0, 1) and the
#matrix: [1.01 0.09 ― 0.09 1.01 ]. Then, multiply the matrix by the point to get a new point. Repeat for a
#total of 200 times. Have your program plot the data points using matplotlib. Be sure to label the x
#and y axes, and include a title. Your title should give a brief description of the shape that the points
#“trace” out.
#Note: the purpose of this activity is to get practice with numpy, so you should use numpy for your
#operations, even if you find it easier to perform this computation a different way