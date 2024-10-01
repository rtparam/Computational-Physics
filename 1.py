# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:03:23 2020

@author: User
"""

import matplotlib.pyplot as plt

n=10000
leftwall=0
rightwall=10
m=10
k=3
dt=0.001
x=[]
v=[0] 
a=[0]
t=[0]


x+=[7] 

def disp(posofx):
    if posofx>=((rightwall-leftwall)/2):
        return -(posofx-((rightwall-leftwall)/2))
    if posofx<=((rightwall-leftwall)/2):
        return (((rightwall-leftwall)/2)-posofx)


for i in range(n):
    Fr=k*(disp(x[i]))
    Fl=k*(disp(x[i]))
    F=Fr+Fl
    a+=[F/m]
    v+=[v[i]+a[i]*dt]
    x+=[x[i]+v[i]*dt]
    t+=[t[i]+dt]

plt.title("1 mass system")
plt.ylabel("position")
plt.xlabel("time")

plt.plot(t,x)




