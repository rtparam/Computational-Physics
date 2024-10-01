# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:21:41 2020

@author: User
"""

import turtle
import math

#take input of number of sides and radius from user
no_of_sides=int(input("Enter number of sides of the regular polygon: "))
r=int(input("Enter the radius of the circle: "))


theta=360/no_of_sides #theta is the inner angle of the polygon

for i in range(no_of_sides): #for loop to make the turtle run
    turtle.forward(2*r*math.sin(theta*math.pi/180*2)) 
 #the angle between the sides and the length of each side is given by the above formula 
    turtle.right(theta) #right moves it by this angle
