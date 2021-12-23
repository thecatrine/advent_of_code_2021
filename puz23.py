with open('puz23.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

map = [[x for x in line] for line in lines]


def can_reach(pos):
    y, x = pos
    if y == 1 and x > 0 and x < len(map[0])-1:
        return True # top line in hallway
    if x in [3, 5, 7, 9] and y in [2, 3]:
        return True # in a room

costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms = {'A': 3, 'B': 5, 'C': 7, 'D': 9}

import copy
def attempt_move(pair, pos1, pos2):
    global rooms
    map, existing_cost = pair

    char = map[pos1[0]][pos1[1]]
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

        if needs_hall:
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
        cost += per

        if map[att[0]][att[1]] == '.':
            tpos = att
        else:
            #import pdb; pdb.set_trace()
            #print("failing move from", pos1, "to", pos2)
            return False, None
    
    new_map = copy.deepcopy(map)
    new_map[pos1[0]][pos1[1]] = '.'
    new_map[pos2[0]][pos2[1]] = char

    return True, (new_map, cost+existing_cost)

HALL = 1
HOME_TOP = 2
HOME_BOT = 3
VALID_STOPS = [1,2,4,6,8,10,11]

def possible_moves(pair, pos):
    map, _ = pair
    char = map[pos[0]][pos[1]]
    moves = []

    #print("considering move for char", char, 'at', pos)

    if pos[0] == HALL:
        # on top line, only consider moving back to correct room
        home = rooms[char]
        if map[HOME_BOT][home] == '.':
            can, new_pair = attempt_move(pair, pos, (HOME_BOT, home))
            if can:
                moves.append(new_pair)
        elif map[HOME_TOP][home] == '.' and map[HOME_BOT][home] == char:
            can, new_pair = attempt_move(pair, pos, (HOME_TOP, home))
            if can:
                moves.append(new_pair)
    elif pos[0] == HOME_TOP or (pos[0] == HOME_BOT and map[HOME_TOP][pos[0]] == '.'):
        # consider moving out of room if not in home
        safe = False
        home = rooms[char]
        if pos[1] == rooms[char]:
            if pos[0] == HOME_BOT:
                safe = True
            if pos[0] == HOME_TOP and map[HOME_BOT][home] == char:
                safe = True

        if not safe:
            spots_to_attempt = [(HALL, x) for x in VALID_STOPS] + [(HOME_BOT, home), (HOME_TOP, home)]
            for spot in spots_to_attempt:
                can, new_pair = attempt_move(pair, pos, spot)
                if can:
                    moves.append(new_pair)
        #else:
            #print(f"{char} is safe at {pos}")
            #print_map(map)
            #import pdb; pdb.set_trace()

    return moves


def all_possible_moves(pair):
    map, _ = pair
    all_poss = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] in ['A', 'B', 'C', 'D']:
                #print("possible move at", (y, x))
                possibles = possible_moves(pair, (y, x))

                #print(len(possibles))
                all_poss += possibles

    return all_poss

def print_map(map):
    for line in map:
        print(''.join(line))


def check_win(map):
    for char in ['A', 'B', 'C', 'D']:
        if map[HOME_TOP][rooms[char]] != char:
            return False
        if map[HOME_BOT][rooms[char]] != char:
            return False
    return True


def map_to_key(map):
    return ''.join([x for line in map for x in line])

cache = {}


pair = (map, 0)
wins = []
possibles = [pair]
i = 0
min_cost = 100000
while len(possibles) > 0:
    i+=1
    pair = possibles.pop()

    map, cost = pair
    key = map_to_key(map)
    if key in cache and cache[key] <= cost:
        continue

    cache[key] = cost

    #print_map(map)
    if cost > 100000:
        continue

    moves = all_possible_moves(pair)
    #import pdb; pdb.set_trace()

    for move in moves:
        move_map = move[0]
        if check_win(move_map):
            wins.append(move)
            if move[1] < min_cost:
                print("best win", move[1])
                min_cost = move[1]
        else:
            possibles.append(move)

    
#print(wins)
print(min_cost)
#new_map, cost = new_pair
#print_map(new_map)
#print(cost)