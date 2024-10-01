# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:25:18 2020

@author: aarathi
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
writer= FFMpegWriter(fps=25, metadata=metadata)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title("10 mass system")

l0, = ax.plot([],[],'k-o')
l1, = ax.plot([],[],'k-o')
l2, = ax.plot([],[],'k-o')
l3, = ax.plot([],[],'k-o')
l4, = ax.plot([],[],'k-o')
l5, = ax.plot([],[],'k-o')
l6, = ax.plot([],[],'k-o')
l7, = ax.plot([],[],'k-o')
l8, = ax.plot([],[],'k-o')
l9, = ax.plot([],[],'k-o')

ax.set_xlim(-5,55)
ax.set_ylim(-5,5)

N=10 #number of masses
pos=[]
v=[]
a=[]
F=[]
t=[0]
dt=0.1
m=10 #3 equal masses
k=3 #2 similar springs
l=5 #length of all springs

for i in range(N):
    pos+=[[i*l]]
    v+=[[0]]
    a+=[[0]]
    F+=[[0]]

#displacing mass 1 to the right by 2 units
pos[0]+=[pos[0][0]+2]

def dleft(x,leftx):
    d=x-leftx-l
    return d
def dright(x,rightx):
    d=x-rightx+l
    return d

with writer.saving(fig,"10 masses.mp4",650):
    for i in range(50):
        x0,y0=0,0
        x1,y1=5,0
        x2,y2=10,0
        x3,y3=15,0
        x4,y4=20,0
        x5,y5=25,0
        x6,y6=30,0
        x7,y7=35,0
        x8,y8=40,0
        x9,y9=45,0

        l0.set_data(x0,y0)
        l1.set_data(x1,y1)
        l2.set_data(x2,y2)
        l3.set_data(x3,y3)
        l4.set_data(x4,y4)
        l5.set_data(x5,y5)
        l6.set_data(x6,y6)
        l7.set_data(x7,y7)
        l8.set_data(x8,y8)
        l9.set_data(x9,y9)

        writer.grab_frame()
    for i in range(50):
        x0=2
        l0.set_data(x0,y0)
        writer.grab_frame()
    for i in range(550):
        F[0]+=[-k*dright(pos[0][-1],pos[1][-1])]
        a[0]+=[F[0][-1]/m]
        F[-1]+=[-k*dleft(pos[-1][-1],pos[-2][-1])]
        a[-1]+=[F[-1][-1]/m]
        
        for j in range(1,N-1):
            F[j]+=[-k*dleft(pos[j][-1],pos[j-1][-1])-k*dright(pos[j][-1],pos[j+1][-1])]
            a[j]+=[F[j][-1]/m]
        for j in range(0,N):
            v[j]+=[v[j][-1]+a[j][-1]*dt]
            pos[j]+=[pos[j][-1]+v[j][-1]*dt]
        t+=[t[-1]+dt]
        
        x0=pos[0][-1]
        x1=pos[1][-1]
        x2=pos[2][-1]
        x3=pos[3][-1]
        x4=pos[4][-1]
        x5=pos[5][-1]
        x6=pos[6][-1]
        x7=pos[7][-1]
        x8=pos[8][-1]
        x9=pos[9][-1]
        
        l0.set_data(x0,y0)
        l1.set_data(x1,y1)
        l2.set_data(x2,y2)
        l3.set_data(x3,y3)
        l4.set_data(x4,y4)
        l5.set_data(x5,y5)
        l6.set_data(x6,y6)
        l7.set_data(x7,y7)
        l8.set_data(x8,y8)
        l9.set_data(x9,y9)

        writer.grab_frame()
