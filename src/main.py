import sys
import os
import random
from subprocess import call
from time import sleep

import person
import tiles
from tile import Tile
from world import World

import click
from prompt_toolkit import print_formatted_text, HTML

# ----Create instances---- #
world = World()
player = person.Player(None,None,"⊠")
box = person.Box(0,0, "▣")
goal = person.Goal(0,0, "▢")
# ----Create instances---- #

# ----Basic variable declaration ---- #
user_move = ""
debug = False
colors = ['ansired','ansiyellow','ansigreen','ansiblue','ansipurple']
random_color_hold = ""
# ----Basic variable declaration ---- #

def random_color():
    """
    Selects a random color 
    from the list of colors
    """
    global random_color_hold
    random_color_hold = random.choice(colors)
    return random_color_hold

def print_colored_text(text):
    """
    Prints colored text with random colors
    text = Text to color.
    """
    global random_color_hold
    print_formatted_text(HTML(''.join(list(map(lambda c: f'<{random_color()}>{c}</{random_color_hold}>', text)))))


def create_play_state():
    """
    Creates play state.
    Gets rows and columns. 
    decides player position
    adds box and goal 
    """


    if world.rows % 2 != 0 and world.columns % 2 != 0: # decides player pos
        player.y = world.rows // 2
        player.x = world.columns // 2
    else:
        player.y = random.randint(1,world.rows-2)
        player.x = random.randint(1, world.columns-2)
    
    box.x = random.randint(2, world.columns-2) # Randomize cordinates 
    box.y = random.randint(2,world.rows-2) # for box and goal 
    
    goal.y = random.randint(2, world.rows-2)
    goal.x = random.randint(2, world.columns-2)
    
    # checks for coordinate overlays 
    if box.y == player.y and box.x == player.x or player.y == goal.y and player.x == goal.x or box.x == goal.x and goal.y == box.y:
        create_play_state() # calls itself if overlays are found
    else:
        pass
    
    # No overlays
    world.grid[player.y][player.x] = f"\033[1;36;10m{player.icon}\033[0m" # adds player
    world.grid[box.y][box.x] = f"\033[1;31;10m{box.icon}\033[0m" # adds box
    world.grid[goal.y][goal.x] = f"\033[1;34;10m{goal.icon}\033[0m" # adds goal

def check_win_status():
    """
    Checks for the win status
    """
    if box.x == goal.x and box.y == goal.y: # IS box over Goal?
        world.clear()
        for i in range(10):
            world.clear()
            print_colored_text("YOU WIN!!!") 
            sleep(0.5)
        sys.exit()   

def update_player():
    """
    Gets user input
    updates player positions
    checks for errors
    """
    global debug 
    print("Direction (w,a,s,d)")
    # this makes it so the user doesnt have to press enter to submit input
    user_move = click.getchar() # it reads the char in the terminal
    world.grid[box.y][box.x] = " "
    world.grid[player.y][player.x] = " "
   
    # ---- UP ---- #
    if user_move == "w": # updates player coords based on input.
        player.y -= 1
        if player.y == box.y and player.x == box.x: # checks for collisions with player
            box.y -= 1
        elif player.y == goal.y and player.x == goal.x: # checks for collisions with player
            player.y += 1
    
    # ---- DOWN ---- #
    elif user_move == "s":
        player.y += 1
        if player.y == box.y and player.x == box.x:
            box.y += 1
        elif player.y == goal.y and player.x == goal.x:
            player.y -= 1

    # ---- RIGHT ---- #
    elif user_move == "d":
        player.x += 1
        if player.y == box.y and player.x == box.x:
            box.x += 1
        elif player.y == goal.y and player.x == goal.x:
            player.x -= 1
        
    # ---- LEFT ---- #
    elif user_move == "a":
        player.x -= 1
        if player.y == box.y and player.x == box.x:
            box.x -= 1
        elif player.y == goal.y and player.x == goal.x:
            player.x += 1

    # ---- QUIT ---- #
    elif user_move == "q":
        sys.exit("Exiting . . .")
    
    # ---- DEBUG ---- #
    elif user_move == "/" or user_move == "o":
        debug = True
    
    # ---- HELP ---- #
    elif user_move == "h":
        world.clear()
        print("h: prints the help screen\n /(o): starts debug\n wasd: movement commands\n q: quits the game. Press x to exit this screen")
        ex = click.getchar()
        if ex == "x":
            world.clear()
            world.display(debug)
    
    # ---- ERROR ---- #
    else:
        print("Error")

    # ---- STOPS THE PLAYER FROM LEAVING THE GRID ---- #
    if player.y == world.rows - 1:
        player.y = 1
    elif player.y < 1:
        player.y = world.rows - 2
    elif player.x == world.columns - 1:
        player.x = 1
    elif player.x < 1:
        player.x = world.columns - 2
    # ---- STOPS THE PLAYER FROM LEAVING THE GRID ---- #

    # --- STOPS THE BOX FROM LEAVING THE GRID ---- #
    elif box.y == world.rows - 1:
        box.y = 1
    elif box.y < 1:
        box.y = world.rows - 2
    elif box.x == world.columns - 1:
        box.x = 1
    elif box.x < 1:
        box.x = world.columns - 2
    # --- STOPS THE BOX FROM LEAVING THE GRID ---- #
    else:
        print("error") 
          
    world.grid[player.y][player.x] = f"\033[1;36;10m{player.icon}\033[0m"
    world.grid[box.y][box.x] = f"\033[1;31;10m{box.icon}\033[0m" # adds box
    updating = False  # if it updates position, the loop stops    
    check_win_status() # checks win status automatically

def quit_screen():
    """
    Quit screen text 
    """
    for i in range(5):
        world.clear() # clear screen
        print_colored_text("Thanks for playing!")
        sleep(0.3) # pauses for 0.30 seconds

def title_screen():
    """
    Title screen text
    ask user if they want to start
    """

    global colors
    play = ""
    title = "Welcome to"

    world.clear() # "welcome to . . ."
    for i in range(4):
        world.clear()
        print(f"{title}" + (" ."*i))
        sleep(0.7)
    # UwU Knot me daddy ~

    for i in range(9): # Loops through colors for title screen
        world.clear() 
        print_colored_text("BLOCK PUSH")
        sleep(0.3)
    
    # Start game?
    print_colored_text("Start game?")
    print("\033[0m",end="")
    play = input("\n(Y/N)\n").lower()

    if play == "y":
        start_game()
    elif play == "n":
        quit_screen()            
    else:
        print("Sorry, thats an invalid input!")

def start_game():
    """
    Starts game
    """
    global debug 

    # ----INSTRUCTIONS----
    print("This is you => \033[1;36;10m⊠")
    print("\033[0m",end="")
    print("This is the box => \033[1;31;10m▣")
    print("\033[0m",end="")
    print("This is the goal => \033[1;34;10m▢")
    print("\033[0m",end="")
    print("This is a wall => \033[1;35;10m▦")
    print("\033[0m",end="")
    print("(It represents the egde of the play space)")
    print("Your goal is to push the box into the goal... Are you ready?\n")
    # ----INSTRUCTIONS----
    
    play = input("(Y/N)\n").lower()

    if play == 'y':
        world.clear() # clear the screen
        create_play_state() # create play state
        while True:
                world.display(player,box,goal,debug) # dislays
                update_player()
                world.clear() # clear the screen
                check_win_status()


    elif play == "n":
        world.clear()
        quit_screen()

title_screen()