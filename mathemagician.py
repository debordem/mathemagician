#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import math
import os

menu = """
*******************************************************
Welcome to the Mathemagician!!!

Enter:
1 to calculate the area of a circle
2 to calculate the area of a square
3 to calculate the area of a triangle
*******************************************************
"""


##############---#################
# Calculcates the area of a circle
##############****#################
def area_of_circle(radius):
    return math.pi * radius**2

##############---#################
# Calculcates the area of a square
##############****#################
def area_of_square():
    #return math.pi * radius**2
    print("area of square")

##############---#################
# Calculcates the area of a triangle
##############****#################
def area_of_triangle():
    #return math.pi * radius**2
    print("area of triangle")

#Control

print (menu)

choice = input("enter a choice 1-3? ")

# a string?
choice = int(choice)

#circle#
if choice == 1:
    radius = int(input("please enter radius"))
    print (area_of_circle(radius))

#square#
if choice == 2:
    #radius = int(input("please enter radius"))
    print (area_of_square())

#triangle#
if choice == 3:
    #radius = int(input("please enter radius"))
    print (area_of_triangle())












