#Christopher Basham
#Phys 301 Project
    #Electric Discharge Model
    #Using Diffusion Limited Aggression

#Package imports
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import random as rand
import imageio as io
import os

from ElecDiff import Walk as W



im_path = 'C:\\Users\\chris\\Documents\\PHYS301\\Electric-Discharge-Using-DLA\\DiffImages'
gif_path = 'C:\\Users\\chris\\Documents\\PHYS301\\Electric-Discharge-Using-DLA'

#Cleans Images File to Prepare for New Images
[os.remove(im_path+'\\'+file) for file in os.listdir(im_path) if file.endswith('.jpg')]
[os.remove(gif_path+'\\'+file) for file in os.listdir(gif_path) if file.endswith('.gif')]

#Creates Square/Canvas
N = 180
maps = np.zeros((N,N))

#Beginning 'Seed' Location
spot = 'c'                  #Specifies Seed Location Start

seedX,seedY = W().SeedStart(N,spot)    #Gets start seed coordinates

maps[seedX,seedY] = 1
maps[seedX-1,seedY] = 1
maps[seedX+1,seedY] = 1
maps[seedX,seedY+1] = 1

#Generation of Walkers & Runs Walk Function
runs = 2000
orig = runs

while runs > 0:
    #Sets Stuck/Edge Boolean
    stuck = False
    edge = False

    loc = W().Walker(N)    #Creates Walker

    while not stuck and not edge:
        loc,stuck,edge = W().CheckWalk(loc,maps,N,stuck,edge)   #'Walks' the particles

        if stuck:
            #Assigns Stuck Particle
            if runs <= int(1/4*orig):
                maps[loc[1],loc[0]] = 4
                colmap = colors.ListedColormap(['white','black','red','blue','green'])
            elif runs <= int(1/2*orig):
                maps[loc[1],loc[0]] = 3
                colmap = colors.ListedColormap(['white','black','red','blue'])
            elif runs <= int(3/4*orig):
                maps[loc[1],loc[0]] = 2
                colmap = colors.ListedColormap(['white','black','red'])
            else:
                maps[loc[1],loc[0]] = 1
                colmap = colors.ListedColormap(['white','black'])

            #Saves Individual Images to Create Full Video w/ Colors
            plt.imsave(f'{im_path}\\{runs}.jpg',maps,cmap=colmap)   
            runs -= 1


#Creates Gif Video for Visualization
with io.get_writer(gif_path+'\\VisualDLA.gif', mode='I',duration = 0.01) as writer:
    for i in range(orig,0,-1):
        writer.append_data(io.imread(im_path+f'\\{i}.jpg'))

colmap = colors.ListedColormap(['black','white','red','yellow','cyan'])
#Shows Final Resulting Plot
plt.matshow(maps,cmap = colmap)
plt.imsave(f'{gif_path}\\ResultDLA.jpg',maps,cmap=colmap)
plt.show()