from math import e


with open('puz20.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        


key = lines[0]




def char(index):
    return key[index]

def index(mmm, pos, default):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    foo = ""

    for dir in dirs:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if mmm.get(new_pos, default):
            foo += '1'
        else:
            foo += '0'

    #print(foo)
    return int(foo, 2)


out = ""
tot = 0

mmm = {}
#print("PIC\n", pic)
for y in range(len(pic)):
    for x in range(len(pic[y])):
        if pic[y][x] == '#':
            mmm[(y, x)] = True
        else:
            mmm[(y, x)] = False

def enhance(mmm, default, grace):
    new_mmm = {}

    for y in range(-grace, len(lines)-1+grace):
        l = ""
        for x in range(-grace, len(lines[1])+grace):
            i = index(mmm, (y, x), default)
            #print(y, x, i)
            new_mmm[(y, x)] = 1 if key[i] == "#" else 0

    return new_mmm



for round in range(50):
    print(round)
    mmm = enhance(mmm, round % 2 == 1, round + 2)
    paint = [x for x in blab.split('\n') if x != '']

print(blab)

tot = 0
for c in blab:
    if c == "#":
        tot += 1
    
        

    
    
print(tot)