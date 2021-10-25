import world as world
from time import sleep 

grid = world.create_grid()

# world.display(grid)

start = ""


def title_screen():
   main = "Welcome to"
   print(f"{main}", end=" ")
   sleep(0.5)
   world.clear()
   print(print(f"{main} .", end=" ")) 
   sleep(0.5)
   world.clear()
   print(print(f"{main} . .", end=" "))
   sleep(0.5)
   world.clear()
   print(print(f"{main} . . .", end=" "))
   sleep(0.5)
   world.clear()
   # UwU Knot me daddy ~
   for i in range():
      #31
      r = 31
      w = 37
      print(f"\033[1;{r};40m B", end="")
      print(f"\033[1;{w};40m L", end="")
      print(f"\033[1;{r};40m O", end="")
      print(f"\033[1;{w};40m C", end="")
      print(f"\033[1;{r};40m K", end="")
      print(" ", end="")
      print(f"\033[1;{w};40m P", end="")
      print(f"\033[1;{r};40m U", end="")
      print(f"\033[1;{w};40m S", end="")
      print(f"\033[1;{r};40m H", end="")
      
title_screen()
