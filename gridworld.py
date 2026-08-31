import numpy as np 
import matplotlib.pyplot as plt


'''
Build a small grid (4x4 or 5x5) where an agent moves cell by cell with a few special cells (goals,traps). The goal is to create the environment.

'''

class Gridworld:

    def __init__ (self, size=4):
        self.size = size
