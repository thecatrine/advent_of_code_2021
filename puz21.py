with open('puz21.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

print(X,Y, lines[0])