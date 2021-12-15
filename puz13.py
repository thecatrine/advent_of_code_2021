with open('puz13.txt') as f:
    lines = f.read().split('\n')

X, Y = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

#print(lines, X, Y)

lines = [x for x in lines if x != '']

def fold(pos, fold):
    if fold[1] == 0:
        # fold along x
        if pos[0] < fold[0]: return pos
        return (2*fold[0] - pos[0], pos[1])
    else:
        if pos[1] < fold[1]: return pos
        return (pos[0], 2*fold[1] - pos[1])

folds = []
points = []

for line in lines:
    if '=' in line:
        a, b = line.split('=')
        if a[-1] == 'x':
            print("fold along x", b)
            pt = (int(b), 0)
        else:
            print("fold along y", b)
            pt = (0, int(b))

        folds.append(pt)
    else:
        x, y = line.split(',')
        points.append((int(x),int(y)))

map = {}

for point in points:
    t = point
    for f in folds:
        t = fold(t, f)

    map[t] = 1


#print(map)
for y in range(0, 30):
    line = ''
    for x in range(0, 30):
        if map.get((x,y), None) is not None:
            line += '#'
        else:
            line += " "
    print(line)