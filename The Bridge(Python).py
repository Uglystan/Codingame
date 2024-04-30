import sys

marque = []

def stacking(pos, lst_mouvement, speed, ind):
    if speed != 0:
        if len(pos) != 4:
            lst_mouvement.append((pos, "UP", speed, ind))
            lst_mouvement.append((pos, "DOWN", speed, ind))
        if speed > 1:
            lst_mouvement.append((pos, "SLOW", speed, ind))
        lst_mouvement.append((pos, "WAIT", speed, ind))
        lst_mouvement.append((pos, "JUMP", speed, ind))
    lst_mouvement.append((pos, "SPEED", speed, ind))

def check_all_case(map, speed, mouvement, x, y):
    if mouvement == "UP":
        for i in range(x, x + speed + 1):
            if map[y - 1][i] == "0":
                return False
        for i in range(x, x + speed - 1 + 1):
            if map[y][i] == "0":
                return False
    elif mouvement == "DOWN":
        for i in range(x, x + speed + 1):
            if map[y + 1][i] == "0":
                return False
        for i in range(x, x + speed - 1 + 1):
            if map[y][i] == "0":
                return False
    elif mouvement == "REST":
        for i in range(x, x + speed + 1):
            if map[y][i] == "0":
                return False
    return True


def update_mvt(map, mouvement, speed):
    new_mvt = []
    action = mouvement[1]

    if action == "UP":
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            if pos[1] - 1 >= 0 and [pos[0] + speed, pos[1] - 1] not in new_mvt:
                    if check_all_case(map,speed, "UP", pos[0], pos[1]) == True:
                        new_mvt.append([pos[0] + speed, pos[1] - 1])
            else:
                if check_all_case(map,speed, "REST", pos[0], pos[1]) == True:
                    new_mvt.append([pos[0] + speed, pos[1]])
    
    elif action == "DOWN":
        mouvement[0].reverse()
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            if pos[1] + 1 < 4 and [pos[0] + speed, pos[1] + 1] not in new_mvt:
                if check_all_case(map, speed, "DOWN", pos[0], pos[1]) == True:
                    new_mvt.append([pos[0] + speed, pos[1] + 1])
                    new_mvt.reverse()
            else:
                if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                    new_mvt.append([pos[0] + speed, pos[1]])
                    new_mvt.reverse()
        mouvement[0].reverse()

    
    elif action == "SLOW":
        speed = speed - 1
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                new_mvt.append([pos[0] + speed, pos[1]])

    elif action == "SPEED":
        speed = speed + 1
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                new_mvt.append([pos[0] + speed, pos[1]])
            
    elif action == "WAIT":
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                new_mvt.append([pos[0] + speed, pos[1]])
            
    elif action == "JUMP":
        for i in range(len(mouvement[0])):
            pos = mouvement[0][i]
            new_mvt.append([pos[0] + speed, pos[1]])
    return((new_mvt, speed, action))




def check_good_mouvement(map, mouvement, speed):
    all_pos = mouvement[0]
    action = mouvement[1]
    new_pos = []
    survive_bike = 0

    if action == "UP":
        for pos in all_pos:
            if pos[1] - 1 >= 0 and [pos[0] + speed, pos[1] - 1] not in new_pos:
                if check_all_case(map,speed, "UP", pos[0], pos[1]) == True:
                    new_pos.append([pos[0] + speed, pos[1] - 1])
                    survive_bike += 1
            else:
                if check_all_case(map,speed, "REST", pos[0], pos[1]) == True:
                    new_pos.append([pos[0] + speed, pos[1]])
                    survive_bike += 1
    
    elif action == "DOWN":
        all_pos.reverse()
        for pos in all_pos:
            if pos[1] + 1 < 4 and [pos[0] + speed, pos[1] + 1] not in new_pos:
                if check_all_case(map, speed, "DOWN", pos[0], pos[1]) == True:
                    new_pos.append([pos[0] + speed, pos[1] + 1])
                    survive_bike += 1
            else:
                if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                    new_pos.append([pos[0] + speed, pos[1]])
                    survive_bike += 1
        all_pos.reverse()
    
    elif action == "SLOW":
        for pos in all_pos:
            if check_all_case(map, speed - 1, "REST", pos[0], pos[1]) == True:
                survive_bike += 1

    elif action == "SPEED":
        for pos in all_pos:
            if check_all_case(map, speed + 1, "REST", pos[0], pos[1]) == True:
                survive_bike += 1
            
    elif action == "WAIT":
        for pos in all_pos:
            if check_all_case(map, speed, "REST", pos[0], pos[1]) == True:
                survive_bike += 1
            
    elif action == "JUMP":
        for pos in all_pos:
            if map[pos[1]][pos[0] + speed] != "0":
                survive_bike += 1

    if survive_bike >= v:
        return (update_mvt(map, mouvement, speed))
    else:
        return (None, speed, None)


end = {}
def backtrack(map, pos, speed, m):
    lst_mouvement = []
    alive = m
    stacking(pos, lst_mouvement, speed, 0)
    while lst_mouvement:
        mouvement = lst_mouvement.pop()
        if mouvement[0][0][0] > len(l0) - 10: #POur cut
            break
        speed = mouvement[2]
        if mouvement not in marque:
            marque.append(mouvement)
            new_mvt, speed, action = check_good_mouvement(map, mouvement, speed)
            if new_mvt != None:
                end[mouvement[3]] = action
                stacking(new_mvt, lst_mouvement, speed, mouvement[3] + 1)

m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
l0 = input() + "................"  # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
l1 = input() + "................"
l2 = input() + "................"
l3 = input() + "................"
map = [l0, l1, l2, l3]
pos = []

i = 0
s = 0
# node_graph = build_graph([l0, l1, l2, l3])
# game loop
while True:
    if i == 0:
        s = int(input())  # the motorbikes' speed
        for i in range(m):
            # x: x coordinate of the motorbike
            # y: y coordinate of the motorbike
            # a: indicates whether the motorbike is activated "1" or detroyed "0"
            x, y, a = [int(j) for j in input().split()]
            pos.append([x, y])
    backtrack(map, pos, s, m)
    for i in end:
        print(end[i])
        s = int(input())  # the motorbikes' speed
        for i in range(m):
            # x: x coordinate of the motorbike
            # y: y coordinate of the motorbike
            # a: indicates whether the motorbike is activated "1" or detroyed "0"
            x, y, a = [int(j) for j in input().split()]
