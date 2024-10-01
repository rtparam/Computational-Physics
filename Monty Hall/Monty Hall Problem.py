# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:10:56 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

N=1000
N_stay=0
N_switch=0

for i in range(N):
    doors=[0,1,2]
    obj=list(np.random.permutation(['G','G','C']))
    contestant=np.random.choice(doors)
    
    doors_sub=doors[:]
    doors_sub.remove(contestant)
    
    if obj[contestant]=='C':
        host=np.random.choice(doors_sub)
    else:
        host_choices=doors[:]
        pos=obj.index('C')
        host_choices.remove(contestant)
        host_choices.remove(pos)
        host=host_choices[0]
        
        
    if obj[contestant]=='C':
        N_stay+=1
    doors_remaining=doors[:]
    doors_remaining.remove(contestant)
    doors_remaining.remove(host)
    if obj[doors_remaining[0]]=='C':
        N_switch+=1
        
print(N_stay/N, N_switch/N)