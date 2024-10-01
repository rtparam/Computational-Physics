# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:49:40 2020

@author: aarathi
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
writer= FFMpegWriter(fps=20, metadata=metadata)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

l, = ax.plot([],[],'k-o')

ax.set_xlim(0,10)
ax.set_ylim(-5,5)


ax.set_title('Mass connected to 2 walls by springs displaced to the right')

x0,y0=5,0
m=10
wall_1=0
wall_2=10
k=3
dt=0.1
x=[] #list keeping track of position of m
#let the mass be at x=5 initially (mean position)
x+=[7] #the mass is displaced to the  right by 2 units
v=[0] #list keeping track of velocity of m
a=[0] #list keeping track of acceleration of m
t=[0]


def disp(xvalue):
    if xvalue>=5:
        return -(xvalue-5)
    if xvalue<=5:
        return (5-xvalue)

with writer.saving(fig,"1 mass.mp4",280):
    for i in range(40):
        l.set_data(x0,0)
        writer.grab_frame()
    for i in range(40):
        x0=7
        l.set_data(x0,0)
        writer.grab_frame()
    for i in range(200):
        F_right=k*(disp(x[i]))
        F_left=k*(disp(x[i]))
        F=F_right+F_left
        a+=[F/m]
        v+=[v[i]+a[i+1]*dt]
        x+=[x[i]+v[i+1]*dt]
        t+=[t[i]+dt]
        
        x0=x[i]+v[i+1]*dt
        l.set_data(x0,0)
        writer.grab_frame()



# plt.plot(t,x)
# plt.plot(t,v)
# plt.plot(t[1:],a[1:])