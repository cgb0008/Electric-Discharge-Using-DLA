#Christopher Basham
#Class Containing All Required Functions

import numpy as np
import random as rand

class Walk():
    def __init__(self):
        '''
            Initializes Class
        '''
    def Walker(self,N,prevloc):
        '''
            N = size of plot
            prevloc = previous stuck piece
        '''
        top_bottom = rand.randint(1,4)
        self.loc = prevloc

        if top_bottom == 1:
              self.walker = [N,rand.randint(1,N)]
        if top_bottom == 2:
              self.walker = [int(N/2),rand.randint(1,N)]
        if top_bottom == 3:
            self.walker = [rand.randint(prevloc[1]-60,prevloc[1]-50),rand.randint(0,prevloc[0])]
        if top_bottom == 4:
            self.walker = [rand.randint(prevloc[1]+50,prevloc[1]+60),rand.randint(0,prevloc[0])]
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
        if ((self.loc[0]+1) > N-1 or (self.loc[1]+1) > N-1 or (self.loc[1]-1) < 1 or (self.loc[0]-1) < 0):
            self.edge = True
        if self.edge:
            self.loc = [rand.randint(int(N/6),int(5*N/6)),rand.randint(int(N/6),int(5*N/6))]
        
        #Changes walker into seed if 'stuck' to previous seed
        if not self.edge:
            up = self.maps[self.loc[1]+1,self.loc[0]]
            down = self.maps[self.loc[1]-1,self.loc[0]]
            left = self.maps[self.loc[1],self.loc[0]-1]
            right = self.maps[self.loc[1],self.loc[0]+1]

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
            k = rand.randint(1,3)
            if k == 1:
                self.loc = [self.loc[1]-1,self.loc[0]]
            if k == 2:
                self.loc = [self.loc[1],self.loc[0]+1]
            if k == 3:
                self.loc = [self.loc[1],self.loc[0]-1]
        
        #Return Needed Values
        return (self.loc,self.stuck,self.edge)