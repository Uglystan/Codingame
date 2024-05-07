import sys
from queue import Queue

def flood_file(map, pos_start_y, pos_start_x, nbr, marque):
    marque.append((pos_start_y, pos_start_x))
    # print(map, file=sys.stderr)
    nbr += 1
    if pos_start_x + 1 < l and map[pos_start_y][pos_start_x + 1] == "O" and (pos_start_y, pos_start_x + 1) not in marque:
        nbr = flood_file(map, pos_start_y, pos_start_x + 1, nbr, marque)
    if pos_start_x - 1 >= 0 and map[pos_start_y][pos_start_x - 1] == "O" and (pos_start_y, pos_start_x - 1) not in marque:
        nbr = flood_file(map, pos_start_y, pos_start_x - 1, nbr, marque)
    if pos_start_y + 1 < h and map[pos_start_y + 1][pos_start_x] == "O" and (pos_start_y + 1, pos_start_x) not in marque:
        nbr = flood_file(map, pos_start_y + 1, pos_start_x, nbr, marque)
    if pos_start_y - 1 >= 0 and map[pos_start_y - 1][pos_start_x] == "O" and (pos_start_y - 1, pos_start_x) not in marque:
        nbr = flood_file(map, pos_start_y - 1, pos_start_x, nbr, marque)
    # print(nbr, file=sys.stderr)
    return nbr

def iter_flood_file(map, pos):
    marque = set()
    waiting = Queue()
    nbr = 0

    waiting.put(pos)

    while not waiting.empty():
        coord = waiting.get()

        if coord in marque:
            continue
        
        marque.add(coord)

        if map[coord[0]][coord[1]] == "O":
            nbr += 1

        if coord[1] + 1 < l and map[coord[0]][coord[1] + 1] == "O" and (coord[0], coord[1] + 1) not in marque:
            waiting.put((coord[0], coord[1] + 1))
        if coord[1] - 1 >= 0 and map[coord[0]][coord[1] - 1] == "O" and (coord[0], coord[1] - 1) not in marque:
            waiting.put((coord[0], coord[1] - 1))
        if coord[0] + 1 < h and map[coord[0] + 1][coord[1]] == "O" and (coord[0] + 1, coord[1]) not in marque:
            waiting.put((coord[0] + 1, coord[1]))
        if coord[0] - 1 >= 0 and map[coord[0] - 1][coord[1]] == "O" and (coord[0] - 1, coord[1]) not in marque:
            waiting.put((coord[0] - 1, coord[1]))
    return nbr

l = int(input())
h = int(input())
map = []

for i in range(h):
    row = input()
    map.append(row)

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    nbr = 0
    marque = [()]
    if map[y][x] != "O":
        print("0")
    else:
        print(iter_flood_file(map, (y, x)))
