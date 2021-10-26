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
        print(f"\033[1;{i + 30};40mB", end="")
        print(f"\033[1;{i + 29};40mL", end="")
        print(f"\033[1;{i + 28};40mO", end="")
        print(f"\033[1;{i + 27};40mC", end="")
        print(f"\033[1;{i + 26};40mK", end="")
        print(" ", end="")
        print(f"\033[1;{i + 25};40mP", end="")
        print(f"\033[1;{i + 24};40mU", end="")
        print(f"\033[1;{i + 23};40mS", end="")
        print(f"\033[1;{i + 22};40mH\n", end="")
        sleep(0.2)
        print("\033[0m",end="")

    play = ""
    # Start game?
    print(f"\033[1;{random.choice(list(colors.values()))}40mS",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}40mt",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}40ma",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}40mr",end="")
    print(f"\033[1;{random.choice(list(colors.values()))}40mt",end="")
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
        print(f"\033[1;{colors.get(random.choice(e))}40mT",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mh",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40ma",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mn",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mk",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40ms",end="")
        print(" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mf",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mo",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mr",end="")
        print(" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mc",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mo",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mm",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mi",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mn",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40mg",end="")
        print(f"\033[1;{colors.get(random.choice(e))}40m!",end="")
        time.sleep(0.3)

def start_game():
    print("This is you => \033[1;36;40m⊠")
    print("\033[0m",end="")
    print("This is the box => \033[1;31;40m▣")
    print("\033[0m",end="")
    print("This is the goal => \033[1;34;40m▢")
    print("\033[0m",end="")
    print("This is a wall => \033[1;35;40m▦")
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