import numpy as np 
import matplotlib.pyplot as plt


'''
Build a small grid (4x4 or 5x5) where an agent moves cell by cell with a few special cells (goals,traps). The goal is to create the environment.

'''

class Gridworld:

    def __init__ (self, size=4):

        self.size = size
        self.goal = 10
        self.trap = -10
        self.map = np.full((size,size), -1)

        self.map[np.random.randint(0,size),np.random.randint(0,size)] = self.goal

        #Can be optimized
        i = np.random.randint(0,size)
        j = np.random.randint(0,size)
        print(type(np.where(self.map == self.goal)))
        print(type(np.where(self.map == self.goal)))

        while self.map[i,j] == self.goal:

            i = np.random.randint(0,size)
            j = np.random.randint(0,size)

        self.map[i,j] = self.trap


    def gridconst(self):
        # pass
        print(self.map)
        print(np.random.randint(self.size))
        
        
if __name__ == "__main__":        

    grid = Gridworld()
    # grid.gridconst()