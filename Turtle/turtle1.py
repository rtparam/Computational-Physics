# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:24:21 2020

@author: User
"""

import turtle
import time

bob=turtle.Turtle()
bob.color("blue")
bob.setposition(0,90)

vx=100
vy=0
g=-9.8
dt=0.1
xx=bob.xcor()
yy=bob.ycor()

while yy>=0:
    xx+=vx*dt
    yy+=vy*dt
    vy+=g*dt
    time.sleep(1)
    bob.goto(xx,yy)
    
turtle.done()
