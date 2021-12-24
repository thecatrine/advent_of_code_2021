with open('puz23.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

map = [[x if x in ['A', 'B', 'C', 'D', '.'] else None for x in line] for line in lines]

mmap = {}
places_to_consider = []
for y in range(Y):
    for x in range(X):
        if map[y][x] in ['A', 'B', 'C', 'D', '.']:
            mmap[(y,x)] = map[y][x]
            places_to_consider.append((y,x))


costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A': 3, 'B': 5, 'C': 7, 'D': 9}


import copy
def attempt_move(pair, pos1, pos2):
    global rooms
    existing_cost, map = pair.priority, pair.item

    char = map[pos1]
    cost = 0
    per = costs[char]

    tpos = pos1

    needs_hall = False
    if pos1[1] != pos2[1]:
        needs_hall = True

    #if pos1 == (2, rooms['B']) and pos2 == (2, rooms['C']):
    #    print("B to C")
    #    import pdb; pdb.set_trace()

    while tpos != pos2:
        if tpos[0] == HALL:
            needs_hall = False

        if needs_hall or tpos[0] > pos2[0]:
            #print('up')
            att = (tpos[0]-1, tpos[1])
        elif tpos[1] > pos2[1]:
            #print('left')
            att = (tpos[0], tpos[1]-1)
        elif tpos[1] < pos2[1]:
            #print('right')
            att = (tpos[0], tpos[1]+1)
        elif tpos[0] < pos2[0]:
            #print('down')
            att = (tpos[0]+1, tpos[1])
        else:
            import pdb; pdb.set_trace()
        cost += per

        if map[att] == '.':
            tpos = att
        else:
            #import pdb; pdb.set_trace()
            #print("failing move from", pos1, "to", pos2)
            return False, None
    
    new_map = copy.deepcopy(map)
    new_map[pos1] = '.'
    new_map[pos2] = char

    return True, Group(cost+existing_cost, new_map)

HALL = 1
HOME_TOP = 2
HOME_BOT = Y - 2
VALID_STOPS = [1,2,  4,  6,  8,  10,11]

def possible_moves(pair, pos):
    _, map = pair.priority, pair.item
    char = map[pos]
    moves = []

    #print("considering move for char", char, 'at', pos)

    #if pos == (1, 10):
        #import pdb; pdb.set_trace()


    if pos[0] == HALL:
        # on top line, only consider moving back to correct room
        home = rooms[char]
        for y in range(HOME_BOT, HOME_TOP-1, -1):
            #print(y, home)
            if map[(y,home)] == '.':
                can, new_pair = attempt_move(pair, pos, (y, home))
                if can:
                    moves.append(new_pair)
                break
            elif map[(y, home)] == char:
                continue
            else:
                break
    else:
        # try to move if not safe
        home = rooms[char]
        safe = pos[1] == home
    
        for y in range(pos[0], HOME_BOT+1):
            if map[(y, home)] != char:
                safe = False
                break
        
#        if safe:
#            print("safe")
#            import pdb; pdb.set_trace()

        if not safe:
            #print("home places", home_places)
            spots_to_attempt = [(HALL, x) for x in VALID_STOPS]
            for spot in spots_to_attempt:
                #if pos == (3, 5) and spot == (1, 6):
                #    import pdb; pdb.set_trace()
                can, new_pair = attempt_move(pair, pos, spot)
                if can:
                    moves.append(new_pair)
        #else:
            #print(f"{char} is safe at {pos}")
            #print_map(map)
            #import pdb; pdb.set_trace()

    return moves


def all_possible_moves(pair):
    _, map = pair.priority, pair.item
    all_poss = []
    for spot in places_to_consider:
        if map[spot] in ['A', 'B', 'C', 'D']:
            possibles = possible_moves(pair, spot)

            #print(len(possibles))
            all_poss += possibles

    return all_poss

def print_map(map):
    for y in range(Y):
        line = ''
        for x in range(X):
            c = map.get((y, x), '#')
            line += c
        print(line)


def check_win(map):
    for char in ['A', 'B', 'C', 'D']:
        for y in range(HOME_TOP, HOME_BOT+1):
            if map[(y, rooms[char])] != char:
                return False
    return True


def print_history(hist):
    print("REPLAY")
    for item in hist:
        print("cost", item.priority)
        print_map(item.item)
        print()

def key_from_map(map):
    return str(map)

cache = {}

print_map(mmap)

import queue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Group:
    priority: int
    item: Any=field(compare=False)

pair = Group(0, mmap)
wins = []
possibles = queue.PriorityQueue()
possibles.put(pair)
i = 0
min_cost = 100000
min_win = None
while not possibles.empty():
    i+=1
    group = possibles.get()
    pair = group

    cost, map = pair.priority, pair.item
    key = key_from_map(map)

    #import pdb; pdb.set_trace()

    #if map == test_map:
    #    import pdb; pdb.set_trace()
    if key in cache and cache[key] <= cost:
        continue

    cache[key] = cost

    #print_map(map)
    if cost > min(50000, min_cost):
        continue
    #if len(group) > 100:
    #    continue

    moves = all_possible_moves(pair)
    #import pdb; pdb.set_trace()

    for move in moves:
        new_group = move

        move_map = move.item
        if check_win(move_map):
            if move.priority < min_cost:
                print("best win", move.priority)
                min_cost = move.priority
                min_win = new_group
        else:
            #print(move)
            possibles.put(move)

    
print_history(min_win)