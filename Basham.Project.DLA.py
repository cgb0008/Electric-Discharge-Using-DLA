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
colmap = colors.ListedColormap(['black','white'])

#Beginning 'Seed'
seedY = int(N/2)
seedX = int(N/2)
maps[seedX,seedY] = 1
maps[seedX-1,seedY] = 1
maps[seedX+1,seedY] = 1
maps[seedX,seedY+1] = 1

#Generation of Walkers & Runs Walk Function
runs = 20
im_num = runs
loc = [N-5,N-5]

while runs > 0:
    #Sets Stuck/Edge Boolean
    stuck = False
    edge = False

    loc = W().Walker(N)    #Creates Walker

    while not stuck and not edge:
        loc,stuck,edge = W().CheckWalk(loc,maps,N,stuck,edge)   #'Walks' the particles

        if stuck:
            #Assigns Stuck Particle
            maps[loc[1],loc[0]] = 1
            
            #Saves Individual Images to Create Full Video
            plt.imsave(f'{im_path}\\{runs}.jpg',maps,cmap=colmap)
            runs -= 1


#Creates Gif Video for Visualization
with io.get_writer(gif_path+'\\VisualDLA.gif', mode='I',duration = 0.01) as writer:
    for i in range(im_num,0,-1):
        writer.append_data(io.imread(im_path+f'\\{i}.jpg'.format(i=i)))


#Shows Final Resulting Plot
plt.matshow(maps,cmap = colmap)
plt.show()