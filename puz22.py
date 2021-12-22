with open('puz22.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

xs = [0, 0]
ys = [0, 0]
zs = [0, 0]

parsed_lines = []

for line in lines:
    #print(line)
    dir, rest = line.split(' ')
    x, y, z = rest.split(',')
    x = [int(xx) for xx in x[2:].split('..')]
    y = [int(xx) for xx in y[2:].split('..')]
    z = [int(xx) for xx in z[2:].split('..')]

    x = (x[0], x[1] + 1)
    y = (y[0], y[1] + 1)
    z = (z[0], z[1] + 1)

    dirx = 1 if x[0] < x[1] else -1
    diry = 1 if y[0] < y[1] else -1
    dirz = 1 if z[0] < z[1] else -1

    if x[0] < xs[0]: xs[0] = x[0]
    if x[1] > xs[1]: xs[1] = x[1]
    if y[0] < ys[0]: ys[0] = y[0]
    if y[1] > ys[1]: ys[1] = y[1]
    if z[0] < zs[0]: zs[0] = z[0]
    if z[1] > zs[1]: zs[1] = z[1]


    parsed_lines.append([dir, x, y, z])

print(xs, ys, zs)

def contained(a, b):
    #print(a, b)
    if a[0][0] >= b[0][0] and a[0][1] <= b[0][1] and \
       a[1][0] >= b[1][0] and a[1][1] <= b[1][1] and \
       a[2][0] >= b[2][0] and a[2][1] <= b[2][1]:
        return True

    return False

def outside(a, b):
    if a[0][1] <= b[0][0] or a[0][0] >= b[0][1]: return True
    if a[1][1] <= b[1][0] or a[1][0] >= b[1][1]: return True
    if a[2][1] <= b[2][0] or a[2][0] >= b[2][1]: return True
    return False

top_cube = {}

blah = {}

import copy 
def count(cube, scale=2**17):
    tot = 0
    new_cube = copy.deepcopy(cube) # ???

    for k, v in new_cube.items():
        if v == 1:
            tot += scale*scale*scale
        elif isinstance(v, dict):
            tot += count(v, scale=scale>>1)

    return tot

highest_contained = 0

def apply(cube, p, val, scale=2**17, offset=(-2**17, -2**17, -2**17), place=0):
    global highest_contained
    new_cube = cube #copy.deepcopy(cube)

    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                box = (
                    (scale*x+offset[0], scale*(x+1)+offset[0]), 
                    (scale*y+offset[1], scale*(y+1)+offset[1]), 
                    (scale*z+offset[2], scale*(z+1)+offset[2]),
                )

                #import pdb; pdb.set_trace()


                #if blah.get((x, y, z, box), None) is not None:
                    #print("Oh no!", (x, y, z, box), scale)
                #    raise Exception("fuck")
                #else:
                #    blah[(x, y, z, box)] = True
                #print(box, p, val, scale)

                if outside(box, p[1:]):
                    #if scale >= highest_contained:
                        #highest_contained = scale
                        #print('outside', scale)
                    #print('outside', p, box)
                    if new_cube.get((x,y,z), None) is None:
                        new_cube[(x, y, z)] = place
                    continue

                if contained(box, p[1:]):
                   # if scale >= highest_contained:
                   #    highest_contained = scale
                    #print('contained', box, p)
                    new_cube[(x, y, z)] = val
                else:
                    exist = new_cube.get((x, y, z), None) 

                    if exist is None:
                        new_cube[(x, y, z)] = {}
                    if isinstance(exist, int):
                        place = exist

                    if isinstance(exist, int):
                        new_cube[(x, y, z)] = {}

                    new_scale = scale >> 1
                    www = new_cube[(x, y, z)]
                    
                    if scale == 1: import pdb; pdb.set_trace()
                    new_cube[(x, y, z)] = apply(
                        www, 
                        p, 
                        val, 
                        scale=new_scale,
                        offset=(box[0][0], box[1][0], box[2][0]),
                        place=place,
                    )
    return new_cube


tot_map = {}
for p in parsed_lines:
    dir, x, y, z = p
    v = 1 if dir == 'on' else 0

    print(p)
    tot_map = apply(tot_map, (v, x, y, z), v)

#print(tot_map)
print(count(tot_map))


def overlap(a, b):
    x0 = max(a[0][0], b[0][0])
    x1 = min(a[0][1], b[0][1])
    if x0 >= x1: return False, []

    y0 = max(a[1][0], b[1][0])
    y1 = min(a[1][1], b[1][1])
    if y0 >= y1: return False, []

    z0 = max(a[2][0], b[2][0])
    z1 = min(a[2][1], b[2][1])
    if z0 >= z1: return False, []
    

    # Decompose into overlapping cubes
    overlap = [[x0, x1], [y0, y1], [z0, z1]]


    

#tot = 0
#
#cube_list = []
#
#for i in range(len(parsed_lines)):
#    p, x, y, z = parsed_lines[i]
#
#    size = (x[1]-x[0] + 1)*(y[1]-y[0] + 1)*(z[1]-z[0] + 1)
#
#    new_size = size
#
#    for existing_cube in cube_list:
#        o = overlap((x, y, z), existing_cube[1:])


        