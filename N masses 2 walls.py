# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:07:06 2020

@author: aarathi
"""

import matplotlib.pyplot as plt

N=10 #number of masses
pos=[]
v=[]
a=[]
F=[]
t=[0]
dt=0.001
m=5 #3 equal masses
k=5 #2 similar springs
l=5 #length of all springs

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.set_title('10 mass system')

for i in range(N+2):
    pos+=[[i*5]]
    v+=[[0]]
    a+=[[0]]
    F+=[[0]]

#displacing mass 1 to the right by 2 units
pos[1]+=[pos[1][0]+2]

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

plt.plot(t,pos[1][1:])

for i in range(2,N+1):
    plt.plot(t,pos[i])
    
fig.savefig('10 masses.jpg')