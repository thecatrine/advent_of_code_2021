with open('puz13.txt') as f:
    lines = f.read().split('\n')

X, Y = len(lines), len(lines[0])        

map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])