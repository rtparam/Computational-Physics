# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:12:13 2020

@author: aarathi
"""

import matplotlib.pyplot as plt

m=10
wall_1=0
wall_2=10
k=3
dt=0.001

x=[] #list keeping track of position of m
#let the mass be at x=5 initially (mean position)
x+=[7] #the mass is displaced to the  right by 2 units
v=[0] #list keeping track of velocity of m
a=[0] #list keeping track of acceleration of m
t=[0]

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

def disp(xvalue):
    if xvalue>=5:
        return -(xvalue-5)
    if xvalue<=5:
        return (5-xvalue)


for i in range(0,100000):
    F_right=k*(disp(x[i]))
    F_left=k*(disp(x[i]))
    F=F_right+F_left
    a+=[F/m]
    v+=[v[i]+a[i+1]*dt]
    x+=[x[i]+v[i+1]*dt]
    t+=[t[i]+dt]

ax.set_title('Mass connected to 2 walls by springs displaced to the right')
ax.set_xlabel('time')

ax.plot(t,x,'b')
ax.plot(t,v,'r')
ax.plot(t[1:],a[1:],'g')

ax.legend(["position","velocity","acceleration"],loc ="upper right")

fig.savefig('1 mass.jpg')
