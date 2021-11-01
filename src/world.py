import tiles
import random
import os
import time
from subprocess import call

class World:

    def __init__(self, rows = 7, collums = 9):
        """
        Intializes the class.
        """
        self.grid = []
        self.rows = rows
        self.collums = collums
    
        # matrix = [[1 if y == 0 or x == 0 or y == rows-1 or x == collums - 1 else 0 for y in range(rows)] for x in range(collums)]
        for y in range(rows): # creates grid * rows
            self.grid.append([])
            for x in range(collums) : # creates grid * collums
                if y == 0 or x == 0 or y == self.rows-1 or x == self.collums - 1: # Wall piece?
                    self.grid[y].append(tiles.wall.icon) 
                else:
                    self.grid[y].append(" ") # Not wall peice
                    
    def display(self, debug = False):
        """
        Displays the grid.
        """ 
        if debug == True:
            print(f"PLAYER COORDS, Y:{player.y} X:{player.x}")
            print(f"BOX COORDS, Y:{box.y} X:{box.x}")
            print(f"GOAL COORDS, Y:{goal.y} X:{goal.x}")
        elif debug == False:
            pass
        else:
            print(f"Debug error. {debug}")
            
        for line in self.grid:
            print(' '.join(map(str,line)))

    def clear(self):
        """
        Clears the terminal.
        """
        call('clear' if os.name =='posix' else 'cls')
