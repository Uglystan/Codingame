import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
i = 0
dir_x = ''
dir_y = ''

def find_dir(dir):
    if len(dir) == 2:
        return dir[1], dir[0]
    else:
        if dir[0] == 'D':
            return "None", dir[0]
        if dir[0] == 'U':
            return "None", dir[0]
        if dir[0] == 'L':
            return dir[0], "None"
        if dir[0] == 'R':
            return dir[0], "None"

min_x = 0
max_x = w
min_y = 0
max_y = h

while True:

    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    dir_x, dir_y = find_dir(bomb_dir)
    if dir_x == 'R':
        min_x = x0
        x0 = math.floor((x0 + max_x) / 2)
    elif dir_x == 'L':
        max_x = x0
        x0 = math.floor((min_x + x0) / 2)
    
    if dir_y == 'D':
        min_y = y0
        y0 = math.floor((y0 + max_y) / 2)
    elif dir_y == 'U':
        max_y = y0
        y0 = math.floor((min_y + y0) / 2)
    print(f"{x0} {y0}")
