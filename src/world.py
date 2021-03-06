import tiles
import random
import os
import time
from subprocess import call

class World:

    def __init__(self, rows = 8, columns = 10):
        """
        Intializes the class.
        """
        self.grid = []
        self.rows = rows
        self.columns = columns
    
        # matrix = [[1 if y == 0 or x == 0 or y == rows-1 or x == columns - 1 else 0 for y in range(rows)] for x in range(columns)]
        for y in range(rows): # creates grid * rows
            self.grid.append([])
            for x in range(columns) : # creates grid * columns
                if y == 0 or x == 0 or y == self.rows-1 or x == self.columns-1: # Wall piece?
                    self.grid[y].append(tiles.wall.icon) 
                else:
                    self.grid[y].append(" ") # Not wall peice
                    
    def display(self,player,box,goal,debug = False):
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
            
        for line in self.grid: # actual display code.
            print(' '.join(map(str,line)))

    def clear(self):
        """
        Clears the terminal.
        """
        call('clear' if os.name =='posix' else 'cls')
