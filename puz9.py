
with open('puz9.txt') as f:
    lines = f.read().split('\n')

map = {}

for y in range(0,len(lines)):
    line = lines[y]
    for x in range(0,len(line)):
        num = int(line[x])
        map[(y,x)] = num


expanding = 11
risks = 0
low_risks = []
for y in range(0,len(lines)):
    for x in range(0,len(lines[0])):
        a = map.get((y-1, x), 10)
        b = map.get((y+1, x), 10)
        c = map.get((y, x-1), 10)
        d = map.get((y, x+1), 10)

        e = map[(y,x)]
        if e < min([a,b,c,d]):
            print(f"low risk at {y},{x}")

            #map[(y,x)] = expanding
            low_risks.append((y,x))
            expanding += 1


def count(map, tup):
    spots = set([tup])
    count = 0
    while not len(spots) == 0:
        spot = spots.pop()
        map[spot] = None
        count += 1
        y,x = spot
        for new_spot in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if map.get(new_spot, None) not in [None, 9]:
                spots |= set([new_spot])
    return count


import functools
print(functools.reduce(lambda x,y: x*y, sorted([count(map, x) for x in low_risks])[-3:] ))

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