#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:02:24 2023

@author: emelie
"""

#%%
import numpy as np

import matplotlib.pyplot as plt

from pathlib import Path



#%%

data10_path = Path('Desktop/Codes/behalf/bin/results/TEST_RUN', 'step_10.dat')
#print(data10_path)
data10 = np.loadtxt(data10_path)
print(data10)
print(np.shape(data10))




data500_path = Path('Desktop/Codes/behalf/bin/results/TEST_RUN', 'step_500.dat')
print(data500_path)
data500 = np.loadtxt(data500_path)


data999_path = Path('Desktop/Codes/behalf/bin/results/TEST_RUN', 'step_999.dat')
print(data999_path)
data999 = np.loadtxt(data999_path)

#%%

x10 = data10[:, 0]
y10 = data10[:, 1]
z10 = data10[:, 2]

#print(x10)

vx10 = data10[:, 3]
vy10 = data10[:, 4]
vz10 = data10[:, 5]


x500 = data500[:, 0]
y500 = data500[:, 1]
z500 = data500[:, 2]

vx500 = data500[:, 3]
vy500 = data500[:, 4]
vz500 = data500[:, 5]


x999 = data999[:, 0]
y999 = data999[:, 1]
z999 = data999[:, 2]

vx999 = data999[:, 3]
vy999 = data999[:, 4]
vz999 = data999[:, 5]

#%%

fig1, ax1 = plt.subplots(2, 2, figsize=(12, 15))

ax1[0, 0].scatter(x10, y10, c='b', s=10)
ax1[0, 0].grid(True)
ax1[0, 0].set_xlabel('x')
ax1[0, 0].set_ylabel('y')
ax1[0, 0].set_title(r'Particles at $t=10$ steps')

ax1[0, 1].scatter(x500, y500, c='b', s=10)
ax1[0, 1].grid(True)
ax1[0, 1].set_xlabel('x')
ax1[0, 1].set_ylabel('y')
ax1[0, 1].set_title(r'Particles at $t=500$ steps')


ax1[1, 0].scatter(x999, y999, c='b', s=10)
ax1[1, 0].grid(True)
ax1[1, 0].set_xlabel('x')
ax1[1, 0].set_ylabel('y')
ax1[1, 0].set_title(r'Particles at $t=999$ steps')


ax1[1, 1].remove()



plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()


#%%


