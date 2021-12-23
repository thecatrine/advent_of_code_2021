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

    x = (x[0], x[1]+1)
    y = (y[0], y[1]+1)
    z = (z[0], z[1]+1)

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



def slicex(b, xaxis):
    if xaxis <= b[0][0] or xaxis >= b[0][1]: return [b]
    shapea = ((b[0][0], xaxis), b[1], b[2])
    shapeb = ((xaxis, b[0][1]), b[1], b[2])
    return [shapea, shapeb]

def slicey(b, yaxis):
    if yaxis <= b[1][0] or yaxis >= b[1][1]: return [b]
    shapea = (b[0], (b[1][0], yaxis), b[2])
    shapeb = (b[0], (yaxis, b[1][1]), b[2])
    return [shapea, shapeb]

def slicez(b, zaxis):
    if zaxis <= b[2][0] or zaxis >= b[2][1]: return [b]
    shapea = (b[0], b[1], (b[2][0], zaxis))
    shapeb = (b[0], b[1], (zaxis, b[2][1]))
    return [shapea, shapeb]

def overlap(a, b):
    x0 = max(a[0][0], b[0][0])
    x1 = min(a[0][1], b[0][1])
    #print(x0, x1)
    if x0 >= x1: 
        return False, []

    y0 = max(a[1][0], b[1][0])
    y1 = min(a[1][1], b[1][1])
    if y0 >= y1: 
        return False, []

    z0 = max(a[2][0], b[2][0])
    z1 = min(a[2][1], b[2][1])
    if z0 >= z1:
        return False, []

    cutsa = (
        x0 if a[0][0] < b[0][0] else x1,
        y0 if a[1][0] < b[1][0] else y1,
        z0 if a[2][0] < b[2][0] else z1
    )
    cutsb = (
        x0 if a[0][0] > b[0][0] else x1,
        y0 if a[1][0] > b[1][0] else y1,
        z0 if a[2][0] > b[2][0] else z1
    )

    return True, (cutsa, cutsb)

def slice(a, cuts):
    slicedx = slicex(a, cuts[0])

    slicedy = []
    for i in slicedx:
        slicedy += slicey(i, cuts[1])
    
    slicedz = []
    for i in slicedy:
        slicedz += slicez(i, cuts[2])

    return slicedz


import copy
all_rects = []

for line in parsed_lines:
    print(line)
    dir, x, y, z = line
    v = 1 if dir == 'on' else 0

    trying_to_add = [(v, (x, y, z))]

    while len(trying_to_add) > 0:
        v, shape = trying_to_add.pop()
        #print("Trying to add", v, shape)
        #print("adding queue", trying_to_add)
        #print("rects", all_rects)

        rects_to_search = all_rects
        all_rects = []
        errored = False
        for existing_rect in rects_to_search:
            if contained(existing_rect[1], shape):
                #import pdb; pdb.set_trace()
                #print("removing", existing_rect)
                continue

            err, results = overlap(existing_rect[1], shape)

            if err:
#                import pdb; pdb.set_trace()

                #overlap
                cutsa, cutsb = results

                smaller_adding = slice(shape, cutsb)
                smaller_rects = slice(existing_rect[1], cutsa)

                #import pdb; pdb.set_trace()

                for j in smaller_rects:
                    should_add_smaller = True
                    for k in smaller_adding:
                        if contained(j, k):
                            should_add_smaller = False
                            break
                    if should_add_smaller:
                        all_rects.append((existing_rect[0], j))

                for j in smaller_adding:
                    trying_to_add.append((v, j))

                errored = True
            else:
                all_rects.append(existing_rect)
        
        if not errored:
            # Finished without error
            #print("Finished without error, adding", shape)
            all_rects.append((v, shape))


print(all_rects)
print(len(all_rects))

tot = 0

for rect in all_rects:
    if rect[0] == 1:
        shape = rect[1]
        tot += (shape[0][1]-shape[0][0]) * (shape[1][1]-shape[1][0]) * (shape[2][1]-shape[2][0])

print(tot)            