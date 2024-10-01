# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:46:45 2020

@author: User
"""

import random
import math

def buffon(n,r,a,b):
    data=[]
    print ('Buffon Needle Experiment ' )
    print ('Runs       Number Hits  estimate of pi')
    for jj in range(r):
        nhits = 0
        for ii in range(n):
            xcent = random.uniform(0,b/2.0)
            theta = random.uniform(0,math.pi/2)
            xtip  = xcent - (a/2.0)*math.cos(theta)  #use of cosine not historically accurate
            if xtip < 0 :
                nhits += 1
        #print str(jj)+'            '+str(nhits)+'               '+str((6.0/a*float(b))*nhits/n)
        c = 2.0*a*n
        d = b*nhits
        print (str(jj)+'            '+str(nhits)+'               '+str(c/d))
        data.append([jj,nhits])
    return data
        

r=5
n=4000
a = 1.5  #needle 2 inches
b = 2  #cracks 2 inch spacing

hits= buffon(n,r,a,b)
    