import sys
import math


# Dans node_map qui est un dict {tuple, [tuple]} je met pour chaque position (y, x) les possibilites
# [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)] a partir de la map que je recois
def update_node_map(map, r, c):
    node_map = {}
    y = 0
    while y < r:
        x = 0
        while x < c:
            if map[y][x] != "#" and map[y][x] != "?":
                key = (y, x)
                node_map[key] = []
                if x + 1 < c and map[y][x + 1] != '#' and map[y][x + 1] != '?' and map[y][x + 1] != 'C':
                    value = (y, x + 1)
                    node_map[key].append(value)
                if x - 1 >= 0 and map[y][x - 1] != '#' and map[y][x - 1] != '?' and map[y][x - 1] != 'C':
                    value = (y, x - 1)
                    node_map[key].append(value)
                if y + 1 < r and map[y + 1][x] != '#' and map[y + 1][x] != '?' and map[y + 1][x] != 'C':
                    value = (y + 1, x)
                    node_map[key].append(value)
                if y - 1 >= 0 and map[y - 1][x] != '#' and map[y - 1][x] != '?' and map[y - 1][x] != 'C':
                    value = (y - 1, x)
                    node_map[key].append(value)
            x += 1
        y += 1
    return (node_map)

def go_to_pos_for_go(pos_for_go, trace, pos):
        instruction = trace.pop()
        if instruction == "LEFT":
            print("RIGHT")
        elif instruction == "RIGHT":
            print("LEFT")
        elif instruction == "UP":
            print("DOWN")
        elif instruction == "DOWN":
            print("UP")

def move(pos, pos_to_go):
    if pos[0] - pos_to_go[0] == -1:
        return "DOWN"
    elif pos[0] - pos_to_go[0] == 1:
        return "UP"
    elif pos[1] - pos_to_go[1] == -1:
        return "RIGHT"
    elif pos[1] - pos_to_go[1] == 1:
        return "LEFT"

def explore_map():
    # Une pile de list avec un tuple et un tuple. Avec Premier tuple possibilite et 2eme tuple
    # position depuis laquelle on a la possibilite
    pile = [] # [()()]
    # Liste de tuple de toute les positions deja visite
    marque = []
    while True:
        map = []
        # kr: row where Rick is located.
        # kc: column where Rick is located.
        kr, kc = [int(i) for i in input().split()]
        pos = (kr, kc)

        for i in range(r):
            row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
            map.append(row)
        node_map = update_node_map(map, r, c)

        # Ajoute des possibiliete pour une pos each_pos liste, pos tuple
        for each_posibilite in node_map[pos]:
            pile.append([each_posibilite, pos])
        # Marque la pos comme visite
        marque.append(pos)
        # tant que pile pas vide:
        while pile:
            # on prend la premiere instruction
            new = pile.pop() # [()()]
            pos_for_go = new[1] # ()
            pos_to_go = new[0] # ()
            # si position ou on doit aller pas marque
            if pos_to_go not in marque:
                # si on est pas sur la position pour aller a la to go
                if pos_for_go != pos:
                    # fonction pour aller a la bonne position
                    go_to_pos_for_go(pos_for_go, trace, pos)
                    # On remet l'instruction dans la pile car pour verifier si on est au bon endroit
                    pile.append(new)
                    break
                # on y vas
                movement = move(pos, pos_to_go)
                if movement == "RIGHT":
                    new_pos = (pos[0], pos[1] + 1)
                elif movement == "LEFT":
                    new_pos = (pos[0], pos[1] - 1)
                elif movement == "UP":
                    new_pos = (pos[0] - 1, pos[1])
                elif movement == "DOWN":
                    new_pos = (pos[0] + 1, pos[1])
                # On ajoute le mouvement dans la liste des mouvements executes
                trace.append(movement)
                for each_posibilite in node_map[new_pos]:
                    pile.append([each_posibilite, new_pos])
                print(movement)
                break
        if not pile:
            return (map, pos)


# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]
trace = []

# game loop
while True:
    tpl = explore_map()
    map = tpl[0]
    pos = tpl[1]
    for row in map:
        print(row, file=sys.stderr)
    print(pos, file=sys.stderr)
        
