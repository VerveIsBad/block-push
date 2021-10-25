from person import Person
import sys
import os
from subprocess import call
import random
from time import sleep

# Randomizes box coordinates
ranX = random.randint(1,5)
ranY = random.randint(1,5)

 # Creates a instance of PLAYER and BOX
player = Person()
box = Person(ranX,ranY)

# randomizes again
ranX = random.randint(1,5)
ranY = random.randint(1,5)

# Creates a instance of the GOAL
goal = Person(ranX,ranY)

box.icon = "box_icon"
goal.icon = "goal_icon"


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
        player.y = Cplayer
        player.x = Cplayer

    # [2,4] == center of default grid

    grid = []
    for i in range(rows): # creates grid * rows
        grid.append([])
        for j in range(collums): # creates grid * collums
            """
            Are you a lollipop? 
            Cause i want to lick you up and down~~
            - Aheryon the floofy boi 
            """
            if i == 0 or j == 0 or i == rows-1 or j == collums - 1:
                grid[i].append(0)
            else:
                grid[i].append(2)

    grid[player.y][player.x] = player.icon # adds player
    grid[box.y][box.x] = box.icon # adds box
    grid[goal.y][goal.x] = goal.icon # adds goal
    return grid

def rainbow():
    """
    clears the terminal
    Generates rainbow 'YOU WIN' text
    clears the terminal
    """
    colors = {
        "red":31,
        "yellow":33,
        "green":32,
        "blue":34,
        "purple":35
    }

    # Please optimize me Verve daddy UwU ~ ~
    e = ['red','yellow','green','blue','purple']
    for i in range(10):
        clear()
        print(f"\033[1;{colors.get(random.choice(e))};40m Y",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40m O",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40m U",end="")
        print(f" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))};40m W",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40m I",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40m N",end="")
        sleep(0.5)

def check_win_status(box,goal):
    """
    Checks for the win status
    """
    if box.x == goal.x and box.y == goal.y:
        clear()
        rainbow()   
        print()
        sys.exit()   

def display(grid, rows = 7, collums = 9):
    """
    Displays the grid.
    """ 
    clear()
    pl="⊠"  # You may think these variables are usless 
    bo="▣" # and you would be right
    go="▢" # but If i remove them the function breaks
    sp=" "  # so here it stays 
    wall="▦" # >~>
    for i in range(rows): 
        for j in range(collums):
            """
            When in dought, piss about.
            - random person from twitter 
            """
            if grid[i][j] == player.icon: # looks or player
                print(f"\033[1;36;40m{pl}", end=" ") 
            elif grid[i][j] == box.icon: # looks or box
                print(f"\033[1;31;40m{bo}", end=" ")
            elif grid[i][j] == goal.icon: # looks or goal
                print(f"\033[1;34;40m{go}", end = " ")
            elif i == 0 or j == 0 or i == rows-1 or j == collums - 1: # looks for edge peices
                print(f"\033[1;35;40m{wall}", end=" ")
            elif not i == 0 or j == 0 or i == rows-1 or j == collums - 1: # finds clear space
                print(f"{sp}", end=" ")
            else:
                print("error")
                sys.exit()
        print()

def move_player(grid, rows = 7, collums = 9, Debug = False):
    """
    Moves the player. Gets input
    sets current player pos to 0
    determines what the input is
    updates player position
    Displays grid.
    """
    user_move = input("Direction (w,a,s,d)\n")
    grid[player.y][player.x] = 0 # sets old player coords to 0
    grid[box.y][box.x] = 0 # I dont remember why i have to do this but i have to.
    
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
    elif Debug == True:
        # UwU You want to see the raw Positons ~ You sussy baka ~
        print(f"PLAYER COORDS, Y:{player.y} X:{player.x}")
        print(f"BOX COORDS, Y:{box.y} X:{box.x}")
        print(f'GOAL COORDS, Y:{goal.y} X:{goal.x}')
    else:
        print("Please select from original prompt\n (w,a,s,d)")
    
    # Starts the update loop.
    updating = True
    
    while updating:
        """
        Checks if the player or box
        Goes past the grid.
        """
        try: # UwU Whats this~? Oh its your error handling ~~  
            grid[player.y][player.x] = player.icon 
            # adds player to grid with updated position 
            grid[box.y][box.x] = box.icon
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
    
        display(grid) # displays grid
