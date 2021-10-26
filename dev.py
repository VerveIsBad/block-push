from time import sleep
import random
import sys
import os
from subprocess import call



def clear():
    """
    Clears the terminal.
    """
    call('clear' if os.name =='posix' else 'cls')




def win_text():
    colors = {
        "red":31,
        "yellow":33,
        "green":32,
        "blue":34,
        "purple":35
    }

    e = ['red','yellow','green','blue','purple']

    for i in range(4):
        clear()
        print(f"\033[1;{colors.get(random.choice(e))};40mY",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40mO",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40mU",end="")
        print(f" ", end="")
        print(f"\033[1;{colors.get(random.choice(e))};40mW",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40mI",end="")
        print(f"\033[1;{colors.get(random.choice(e))};40mN",end="\n")
        sleep(0.3)
win_text()