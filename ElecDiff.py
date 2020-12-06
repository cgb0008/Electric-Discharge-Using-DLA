#Christopher Basham
#Class Containing All Required Functions

import numpy as np
import random as rand

class Walk():
    def __init__(self):
        '''
            Initializes Class
        '''
    def Walker(self,N):
        '''
            N = size of plot
        '''
        position = rand.randint(1,4)
        self.walker = [N-5,N-5]
        
        if position == 1:
            self.walker = [rand.randint(10,int(N/4)),rand.randint(10,N-5)]        #Top Quarter
        if position == 2:
            self.walker = [rand.randint(int(3*N/4),N-5),rand.randint(10,N-5)]    #Bottom Quarter
        if position == 3:
            self.walker = [rand.randint(10,N-5),rand.randint(10,int(N/4))]        #Left Quarter
        if position == 4:
            self.walker = [rand.randint(10,N-5),rand.randint(int(3*N/4),N-5)]    #Right Quarter
        return self.walker

    def CheckWalk(self,loc,maps,N,stuck,edge):
        '''
            Walks particle until it matches with another seed

            Loc = Location of Walker
            Map = Matrix of seeds
            N = size of plot
        '''
        #Creates class var
        self.loc = loc
        self.maps = maps
        self.N = N

        #Creates Boolean Vals
        self.stuck = stuck
        self.edge = edge

        #Checks if Walker is close to edge of square
        if ((self.loc[0]+1) >= N-1 or (self.loc[1]+1) >= N-1 or (self.loc[1]-1) <= 1 or (self.loc[0]-1) <= 1):
            self.edge = True
        if self.edge:
            self.loc = [rand.randint(10,N-10),rand.randint(10,N-10)]
            self.edge = False
        
        #Changes walker into seed if 'stuck' to previous seed
        if not self.edge:
            up = self.maps[self.loc[0]+1,self.loc[1]]
            down = self.maps[self.loc[0]-1,self.loc[1]]
            left = self.maps[self.loc[0],self.loc[1]-1]
            right = self.maps[self.loc[0],self.loc[1]+1]

            if down == 1:
                self.stuck = True
            if up == 1:
                self.stuck = True
            if left == 1:
                self.stuck = True
            if right == 1:
                self.stuck = True
        
        #'Walks' particle if not stuck to another seed
        if not self.stuck and not self.edge:
            k = rand.randint(1,4)
            if k == 1:                          #Up
                self.loc = [self.loc[0]-1,self.loc[1]]
            if k == 2:                          #Right
                self.loc = [self.loc[0],self.loc[1]+1]
            if k == 3:                          #Left
                self.loc = [self.loc[0],self.loc[1]-1]
            if k == 4:                          #Down
                self.loc = [self.loc[0]+1,self.loc[1]]
        
        #Return Needed Values
        return (self.loc,self.stuck,self.edge)