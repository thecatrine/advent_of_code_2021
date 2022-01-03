with open('puz25.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

rights = {}
downs = {}

for y in range(Y):
    for x in range(X):
        if lines[y][x] == 'v':
            downs[(y,x)] = True
        if lines[y][x] == '>':
            rights[(y,x)] = True


def pp(rights, downs):
    map = [['.' for x in range(X)] for y in range(Y)]
    for y,x in rights.keys():
        map[y][x] = '>'
    for y,x in downs.keys():
        map[y][x] = 'v'
    for y in map:
        print(''.join(y))

steps = 0
go = True
import copy
while go:
    go = False

    new_rights = {}
    for right in rights.keys():
        if rights[right]:
            y, x = right
            new_x = x + 1
            if new_x == X: new_x = 0
            if downs.get((y, new_x), None) or rights.get((y, new_x), None):
                new_rights[(y, x)] = True
            else:
                new_rights[(y, x)] = None
                new_rights[(y, new_x)] = True
                #print("x moved")
                go = True
    
    rights = new_rights
    
    new_downs = {}
    for down in downs.keys():
        if downs[down]:
            y, x = down
            new_y = y + 1
            if new_y == Y: new_y = 0
            if downs.get((new_y, x), None) or rights.get((new_y, x), None):
                new_downs[(y, x)] = True
            else:
                new_downs[(y, x)] = None
                new_downs[(new_y, x)] = True
                go = True

    downs = new_downs
    steps += 1

    pp(rights, downs)
    print('')


print(steps)