#Christopher Basham
#Phys 301 Project
    #Electric Discharge Model
    #Using Diffusion Limited Aggression

#Package imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import random as rand
import imageio

from ElecDiff import Walk as W

#Creates Square/Canvas
N = 180
maps = np.zeros((N,N))
colmap = colors.ListedColormap(['black','white'])

#Beginning 'Seed'
seedY = int(N/2)
seedX = 5
maps[seedX,seedY] = 1
maps[seedX-1,seedY] = 1
maps[seedX+1,seedY] = 1
maps[seedX,seedY+1] = 1
maps[seedX+1,seedY+1] = 1
#Generation of # Walkers
runs = 20000
loc = [30,90]

while runs > 0:
    #Sets Stuck Boolean
    stuck = False
    edge = False

    while not stuck and not edge:
        locs = W().Walker(N,loc)    #Creates Walker
        loc,stuck,edge = W().CheckWalk(locs,maps,N,stuck,edge)

        if stuck:
            maps[locs[1],locs[0]] = 1.
            runs -= 1





plt.matshow(maps,interpolation='nearest',cmap = colmap)
plt.show()