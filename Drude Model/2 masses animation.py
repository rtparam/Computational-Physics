# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:58:01 2020

@author: aarathi
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
writer= FFMpegWriter(fps=25, metadata=metadata)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

l0, = ax.plot([],[],'k-o')
l1, = ax.plot([],[],'k-o')

ax.set_xlim(0,15)
ax.set_ylim(-5,5)

ax.set_title('2 Masses connected to walls by 3 springs')

N=2 #number of masses
pos=[]
v=[]
a=[]
F=[]
t=[0]
dt=0.1
m=10 #3 equal masses
k=3 #2 similar springs
l=5 #length of all springs

for i in range(N+2):
    pos+=[[i*5]]
    v+=[[0]]
    a+=[[0]]
    F+=[[0]]

#displacing mass 1 to the right by 2 units
pos[1]+=[pos[1][0]+2]
pos[2]+=[pos[2][0]-2]


def dleft(x,leftx):
    d=x-leftx-l
    return d
def dright(x,rightx):
    d=x-rightx+l
    return d

with writer.saving(fig,"2 masses with walls-2.mp4",550):
    for i in range(50):
        x0,y0=5,0
        x1,y1=10,0
        l0.set_data(x0,y0)
        l1.set_data(x1,y1)
        writer.grab_frame()
    for i in range(50):
        x0=7
        x1=8
        l0.set_data(x0,y0)
        l1.set_data(x1,y1)
        writer.grab_frame()
    for i in range(400):
        for j in range(1,N+1):
            F[j]+=[-k*dleft(pos[j][-1],pos[j-1][-1])-k*dright(pos[j][-1],pos[j+1][-1])]
            a[j]+=[F[j][-1]/m]
            v[j]+=[v[j][-1]+a[j][-1]*dt]
            pos[j]+=[pos[j][-1]+v[j][-1]*dt]
        t+=[t[-1]+dt]
        
        x0=pos[1][-1]
        x1=pos[2][-1]
        
        l0.set_data(x0,y0)
        l1.set_data(x1,y1)

        writer.grab_frame()
