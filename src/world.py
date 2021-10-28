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

    def win_text(self):
        colors = {
            "red":31,
            "yellow":33,
            "green":32,
            "blue":34,
            "purple":35
        }

        e = ['red','yellow','green','blue','purple']

        for i in range(6):
            self.clear()
            print(f"\033[1;{colors.get(random.choice(e))};10mY\033[0m\033[1;{colors.get(random.choice(e))};10mo\033[0m\033[1;{colors.get(random.choice(e))};0mu\033[0m",end="")
            print(f" ", end="") # \033[0m
            print(F"\033[1;{colors.get(random.choice(e))};10mw\033[0m \033[1;{colors.get(random.choice(e))};10mi\033[0m \033[1;{colors.get(random.choice(e))};10mn\033[0m \033[1;{colors.get(random.choice(e))};10m!\033[0m")
            time.sleep(0.2)

    def clear(self):
        """
        Clears the terminal.
        """
        call('clear' if os.name =='posix' else 'cls')
