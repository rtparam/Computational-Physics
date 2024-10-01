# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 16:17:18 2020

@author: User
"""

import matplotlib.pyplot as plt

N=2 

pos=[[0],[5],[10],[15]] 
v=[[0],[0],[0],[0]] 
a=[[],[0],[0],[0]]
F=[[],[0],[0],[]]
t=[0]
dt=0.001
m=10 
k=3 
l=5 

pos[1]+=[pos[1][0]+2]
pos[2]+=[pos[2][0]-2]

def dleft(x,leftx):
    d=x-leftx-l
    return d
def dright(x,rightx):
    d=x-rightx+l
    return d

for i in range(100000):
    for j in range(1,N+1):
        F[j]+=[-k*dleft(pos[j][-1],pos[j-1][-1])-k*dright(pos[j][-1],pos[j+1][-1])]
        a[j]+=[F[j][-1]/m]
        v[j]+=[v[j][-1]+a[j][-1]*dt]
        pos[j]+=[pos[j][-1]+v[j][-1]*dt]
    t+=[t[-1]+dt]

plt.plot(t,pos[1][1:],'b')
plt.plot(t,pos[2][1:],'g')

plt.xlabel("position")
plt.ylabel("time")
plt.title("2 mass system: case 2")
plt.legend(["mass 2","mass 1"])


