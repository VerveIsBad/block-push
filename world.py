from person import Person
import sys
import os
from subprocess import call
import random
from time import sleep

# Randomizes box coordinates
ranY = 0
ranX = 0

# Creates a instance of PLAYER and BOX
player = Person(None,None,"⊠")
box = Person(ranX,ranY, "▣")

# Creates a instance of the GOAL
goal = Person(ranX,ranY, "▢")

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

    box.x = random.randint(1, collums-1) # Randomize cordinates 
    box.y = random.randint(1,rows-1) # for box and goal 

    goal.y = random.randint(1, rows-1)
    goal.x = random.randint(1, collums-1)

    # checks for coordinate overlays 
    if box.y == player.y and box.x == player.x or player.y == goal.y and player.x == goal.x or box.x == goal.x and goal.y == box.y:
        create_play_state(grid)
    else:
        pass

    grid[player.y][player.x] = f"\033[1;36;10m{player.icon}\033[0m" # adds player
    grid[box.y][box.x] = f"\033[1;31;10m{box.icon}\033[0m" # adds box
    grid[goal.y][goal.x] = f"\033[1;34;10m{goal.icon}\033[0m" # adds goal

def win_text():
    colors = {
        "red":31,
        "yellow":33,
        "green":32,
        "blue":34,
        "purple":35
    }

    e = ['red','yellow','green','blue','purple']

    for i in range(6):
        clear()
        print(f"\033[1;{colors.get(random.choice(e))};10mY\033[0m\033[1;{colors.get(random.choice(e))};10mo\033[0m\033[1;{colors.get(random.choice(e))};0mu\033[0m",end="")
        print(f" ", end="") # \033[0m
        print(F"\033[1;{colors.get(random.choice(e))};10mw\033[0m \033[1;{colors.get(random.choice(e))};10mi\033[0m \033[1;{colors.get(random.choice(e))};10mn\033[0m \033[1;{colors.get(random.choice(e))};10m!\033[0m")
        sleep(0.2)

def check_win_status(box,goal):
    """
    Checks for the win status
    """
    if box.x == goal.x and box.y == goal.y:
        clear()
        win_text()   
        print()
        sys.exit()   

def display(grid, debug = False):
    """
    Displays the grid.
    """ 
    clear()
    if debug == True:
        print(f"PLAYER COORDS, Y:{player.y} X:{player.x}")
        print(f"BOX COORDS, Y:{box.y} X:{box.x}")
        print(f'GOAL COORDS, Y:{goal.y} X:{goal.x}')
    else:
        pass

    for line in grid:
        print(' '.join(map(str,line)))

def check_for_errors(grid,player,box):
    """
    Checks if the player or box
    Goes past the grid.
    """
    updating = True
    while updating:

        try: # UwU Whats this~? Oh its your error handling ~~  
            # adds player and box to grid with updated position 
            grid[player.y][player.x] = f"\033[1;36;10m{player.icon}\033[0m"
            grid[box.y][box.x] = f"\033[1;31;10m{box.icon}\033[0m" # adds box
            check_win_status(box, goal) 
            updating = False 
        except IndexError: # i-its so big~~
            # POSSIBLE PLAYER COORDINATE ERRORS
            if player.y == rows:
                player.y = 0
            elif player.y < 0:
                player.y = rows - 1
            elif player.x == collums:
                player.x = 0
            elif player.x < 0:
                player.x = collums - 1
            # POSSIBLE BOX COORDINATE ERRORS
            elif box.y == rows:
                box.y = 0
            elif box.y < 0:
                box.y = rows - 1
            elif box.x == collums:
                box.x = 0
            elif box.x < 0:
                box.x = collums - 1
            else:
                print("error")       

def move_player(grid, rows = 7, collums = 9, debug = False):
    """
    Moves the player. Gets input
    sets current player pos to 0
    determines what the input is
    updates player position
    Displays grid.
    """
    user_move = input("Direction (w,a,s,d)\n")
    grid[player.y][player.x] = " " # sets old player coords to 0
    grid[box.y][box.x] = " " # I dont remember why i have to do this but i have to.
    
    if user_move == "w": # updates player coords based on input.
        player.y -= 1
        # checks for goal and box collision 
        if player.y == box.y and player.x == box.x: # box collision detection 
            box.y -= 1
        elif player.y == goal.y and player.x == goal.x: # goal collision detection 
            player.y += 1

    elif user_move == "s":
        player.y += 1
        # checks for goal and box collision 
        if player.y == box.y and player.x == box.x:
            box.y += 1
        elif player.y == goal.y and player.x == goal.x:
            player.y -= 1

    elif user_move == "d":
        player.x += 1
        # checks for goal and box collision 
        if player.y == box.y and player.x == box.x:
            box.x += 1
        elif player.y == goal.y and player.x == goal.x:
            player.x -= 1

    elif user_move == "a":
        player.x -= 1
        # checks for goal and box collision 
        if player.y == box.y and player.x == box.x:
            box.x -= 1
        elif player.y == goal.y and player.x == goal.x:
            player.x += 1

    elif user_move == "stop":
        sys.exit()
    elif debug == True or user_move == "start debug":
        # UwU You want to see the raw Positons ~ You sussy baka ~
        print(f"PLAYER COORDS, Y:{player.y} X:{player.x}")
        print(f"BOX COORDS, Y:{box.y} X:{box.x}")
        print(f'GOAL COORDS, Y:{goal.y} X:{goal.x}')
    else:
        print("Please select from original prompt\n (w,a,s,d)")
    