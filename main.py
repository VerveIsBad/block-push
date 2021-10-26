import world as world
from time import sleep 
import random 

grid = world.create_grid()

e = ['red','yellow','green','blue','purple']

colors = {
    "red":31,
    "yellow":33,
    "green":32,
    "blue":34,
    "purple":35
}

def title_screen():
    global e
    global colors
    title = "Welcome to"

    world.clear()
    print(f"{title} .", flush = True)
    sleep(1)
    world.clear()
    print(f"{title} . .", flush = True)
    sleep(1)
    world.clear()
    print(f"{title} . . .", flush = True)
    sleep(1)
    # UwU Knot me daddy ~
    
    for i in range(9):
        world.clear()
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

    play = ""

    print(f"\033[1;{colors.get(random.choice(e))}40mS",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40mt",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40ma",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40mr",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40mt",end="")
    print(" ",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40mG",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40ma",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40mm",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40me",end="")
    print(f"\033[1;{colors.get(random.choice(e))}40m?",end="")
    input("\n(Y/N)\n")

    if play == "Y":
        start_game()
    elif play == "N":
        for i in range(5):
            world.clear()
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
    else:
        print("Sorry, thats an invaid input!")

def start_game():
    world.display(grid)
    while True:
        move_player()

title_screen()