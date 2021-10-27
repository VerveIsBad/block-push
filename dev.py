from time import sleep
import random
import sys
import os
from person import Person
from subprocess import call

grid = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]



# Randomizes box coordinates
ranY = 0
ranX = 0

 # Creates a instance of PLAYER and BOX
player = Person()
box = Person(ranX,ranY)


# Creates a instance of the GOAL
goal = Person(ranX,ranY,"⊠")

box.icon = "▣"
goal.icon = "▢"


def clear():
    """
    Clears the terminal.
    """
    call('clear' if os.name =='posix' else 'cls')


def create_grid(rows = 7, collums = 9):
    """
    decides player starting position 
    Creates the grid 
    adds player to grid
    """
    if rows % 2 != 0 and collums % 2 != 0: # decides player pos
        player.y = rows // 2
        player.x = collums // 2
    else:
        player.y = random.randint(1,rows)
        player.x = random.randint(1, collums)


    grid = [] # defines grid 

    for i in range(rows): # creates grid * rows
        grid.append([])
        for j in range(collums): # creates grid * collums
            """
            Are you a lollipop? 
            Cause i want to lick you up and down~~
            - Aheryon the floofy boi 
            """
            if i == 0 or j == 0 or i == rows-1 or j == collums - 1:
                grid[i].append("▦")
            else:
                grid[i].append(" ")

    create_play_state(grid)

    return grid

def create_play_state(grid, rows = 7, collums = 9):
    """
    Creates the play state.
    Coding is stupid. Fuck my life.
    """

    box.x = random.randint(1, collums-1)
    box.y = random.randint(1,rows-1)

    goal.y = random.randint(1, rows-1)
    goal.x = random.randint(1, collums-1)

    grid[player.y][player.x] = player.icon

    if box.y == player.y and box.x == player.x or player.y == goal.y and player.x == goal.x or box.x == goal.x and goal.y == box.y:
        create_play_state(grid)
    else:
        pass

    grid[player.y][player.x] = player.icon # adds player
    grid[box.y][box.x] = box.icon # adds box
    grid[goal.y][goal.x] = goal.icon # adds goal

# Randomizes box coordinates
ranY = 0
ranX = 0
 # Creates a instance of PLAYER and BOX
player = Person(None,None,"⊠")
box = Person(ranX,ranY)
# Creates a instance of the GOAL
goal = Person(ranX,ranY)
box.icon = "▣"
goal.icon = "▢"

grid = create_grid()


for line in grid:
    print (' '.join(map(str, line)))
