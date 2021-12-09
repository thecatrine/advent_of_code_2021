
with open('puz9.txt') as f:
    lines = f.read().split('\n')

map = {}

for y in range(0,len(lines)):
    line = lines[y]
    for x in range(0,len(line)):
        num = int(line[x])
        map[(y,x)] = num




def tups(y,x):
    return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

def count(map, spots, count):
    while spots:
        y,x = spots.pop(); map[(y,x)] = 9; count += 1
        [spots.add(new_spot) for new_spot in tups(y,x) if map.get(new_spot, 9) != 9]
    return count

low_risks = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if map[(y,x)] < min([map.get(tup, 10) for tup in tups(y,x)]):
            low_risks.append(count(map, set([(y,x)]), 0))

import functools
print(functools.reduce(lambda x,y: x*y, sorted(low_risks)[-3:] ))

#changing = True
#while changing:
#    changing = False
#    for y in range(0,len(lines)):
#        for x in range(0,len(lines[0])):
#            a = map.get((y-1, x), 10)
#            b = map.get((y+1, x), 10)
#            c = map.get((y, x-1), 10)
#            d = map.get((y, x+1), 10)
#
#            exp = max([a,b,c,d])
#            if exp > 10 and map[(y,x)] not in [9, exp]:
#                map[(y,x)] = exp
#                changing = True
#
#counts = {}
#for item in map.values():
#    counts.setdefault(item, 0)
#    counts[item] += 1
#
#counts[9] = 0
#
#for i in range(0, len(lines)):
#    l = ""
#    for j in range(0, len(lines[0])):
#        l += str(map[(i,j)]) + " "
#    print(l)
#
#s = sorted(counts.values())
#print(s)
#s = s[-3:]
#print(s[0]*s[1]*s[2])