import random
from time import sleep

grid = [[0 for y in range(6)] for x in range(6)]

grid[-1][-1] = 1
print(grid[-1][-1])
for line in grid:
    print(" ".join(map(str, line)))

