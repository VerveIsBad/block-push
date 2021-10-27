import world as world
from time import sleep 
import random
import sys 

grid = world.create_grid()

e = ['red','yellow','green','blue','purple']

colors = {
    "red":31,
    "yellow":33,
    "green":32,
    "blue":34,
    "purple":35
}

print(colors['red'])

def title_screen():
    """
    Title screen text
    """

    global e
    global colors
    title = "Welcome to"

    world.clear() # "welcome to . . ."
    print(f"{title} .")
    sleep(1)
    world.clear()
    print(f"{title} . .")
    sleep(1)
    world.clear()
    print(f"{title} . . .")
    sleep(1)
    # UwU Knot me daddy ~

    for i in range(9):  #  Bad colored text code. Very bad, extremely slow. 
        world.clear() # BLOCK PUSH

        #
        print(f"\033[1;{i + 30};10mB", end="")
        print(f"\033[1;{i + 29};10mL", end="")
        print(f"\033[1;{i + 28};10mO", end="")
        print(f"\033[1;{i + 27};10mC", end="")
        print(f"\033[1;{i + 26};10mK", end="")
        print(" ", end="")
        print(f"\033[1;{i + 25};10mP", end="")
        print(f"\033[1;{i + 24};10mU", end="")
        print(f"\033[1;{i + 23};10mS", end="")
        print(f"\033[1;{i + 22};10mH\n", end="")
        sleep(0.2)
        print("\033[0m",end="")

    play = ""
    # Start game?
    print(f"\033[1;{random.choice(list(colors.values()))}10mS",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}10mt",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}10ma",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}10mr",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}10mt",end="")
    print(" ",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}0mG",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}0ma",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}0mm",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}0me",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}0m?",end="")
    print("\033[0m",end="")
    play = input("\n(Y/N)\n").lower()

    if play == "y":
        start_game()
    elif play == "n":
        quit_screen()            
    else:
        print("Sorry, thats an invaid input!")

def quit_screen():
    for i in range(5):
        world.clear()
        # Thanks for coming!
        print(f"\033[1;{colors.get(random.choice(e))}10mT",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mh",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10ma",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mn",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mk",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10ms",end="")
        print(" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mf",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mo",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mr",end="")
        print(" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mc",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mo",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mm",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mi",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mn",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10mg",end="")
        print(f"\033[1;{colors.get(random.choice(e))}10m!",end="")
        time.sleep(0.3)

def start_game():
    print("This is you => \033[1;36;10m⊠")
    print("\033[0m",end="")
    print("This is the box => \033[1;31;10m▣")
    print("\033[0m",end="")
    print("This is the goal => \033[1;34;10m▢")
    print("\033[0m",end="")
    print("This is a wall => \033[1;35;10m▦")
    print("\033[0m",end="")
    print("(It represents the egde of the play space)")
    print("Your goal is to push the box into the goal...are you ready?\n")
    play = input("(Y/N)\n").lower()
    if play == "y": 
        world.display(grid)
        while True:
            world.move_player(grid)
    elif play == "n":
        quit_screen()
        sys.exit()
    else:
        print("Invalid input.")


title_screen()