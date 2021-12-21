with open('puz15.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

X, Y = len(lines), len(lines[0])        

map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

def ppp(map):
    for y in range(Y*5):
        line = ''
        for x in range(X*5):
            line += str(displace(map, y, x))
        print(line)

def displace(map, y, x):
    big_y = y // Y
    big_x = x // X

    i = map[(y % Y, x % X)]

    i = i + big_y + big_x
    while i > 9:
        i -= 9

    return i

ppp(map)


pos = (Y*5-1, X*5-1)
pos_to_eval = set([pos])

scores = {}
scores[pos] = displace(map, pos[0], pos[1])
print(scores)


i = 0
while len(pos_to_eval) > 0:
    pos = pos_to_eval.pop()

    i += 1
    if i % 100000 == 0:
        print(pos)

    dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    valid = [(pos[0] + x[0], pos[1] + x[1]) for x in dirs]
    valid = [x for x in valid if x[0] >= 0 and x[1] >= 0 and x[0] < Y*5 and x[1] < X*5]

    #print(score_for_pos)
    for x in valid:
        score_for_pos = displace(map, x[0], x[1]) + scores[pos]
        if x not in scores or score_for_pos <= scores[x]:
            scores[x] = score_for_pos
            pos_to_eval.add(x)

print(scores[(0,0)] - displace(map, 0, 0))


