from pprint import pprint as pp
import numpy as np

with open('puz19.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

scanners = []
for line in lines:
    if line.startswith('---'):
        scanners.append([])
    else:
        x, y, z = [int(x) for x in line.split(',')]
        scanners[-1].append((x, y, z))


for i in range(len(scanners)):
    scanners[i] = set(scanners[i])


# grabbed from internet
from math import pi ,sin, cos

def R(theta, u):
    m = [[cos(theta) + u[0]**2 * (1-cos(theta)), 
             u[0] * u[1] * (1-cos(theta)) - u[2] * sin(theta), 
             u[0] * u[2] * (1 - cos(theta)) + u[1] * sin(theta)],
            [u[0] * u[1] * (1-cos(theta)) + u[2] * sin(theta),
             cos(theta) + u[1]**2 * (1-cos(theta)),
             u[1] * u[2] * (1 - cos(theta)) - u[0] * sin(theta)],
            [u[0] * u[2] * (1-cos(theta)) - u[1] * sin(theta),
             u[1] * u[2] * (1-cos(theta)) + u[0] * sin(theta),
             cos(theta) + u[2]**2 * (1-cos(theta))]]

    return [[int(x) for x in y] for y in m]


rot = R(pi/2, (0, 1, 0))
print(rot)
print(np.matmul(rot, (1, 0, 0)))

def all_pos_2():
    x_rots = []
    possible_angles = [0, pi/2, pi, 3*pi/2]

    for angle in possible_angles:
        rot = R(angle, (1, 0, 0))
        x_rots.append(rot)

    y_rots = []
    for old_rot in x_rots:
        for angle in possible_angles:
            rot = R(angle, (0, 1, 0))
            new_rot = np.matmul(old_rot, rot)
            y_rots.append(new_rot)

    z_rots = []
    for old_rot in y_rots:
        for angle in possible_angles:
            rot = R(angle, (0, 0, 1))
            new_pt = np.matmul(rot, old_rot)
            
            good = True
            for pt in z_rots:
                if np.array_equal(pt, new_pt):
                    good = False
                    break
            if good:
                z_rots.append(new_pt)
    
    return z_rots

def all_pos(pt):
    rotated = []
    swaps = [[0, 1, 2], [1, 2, 0], [2, 0, 1], [0, 2, 1], [1, 0, 2], [2, 1, 0]]
    # axis can be swapped
    for swap in swaps:
        new_pt = [pt[i] for i in swap]
        rotated.append(new_pt)

    # axis can be flipped
    flipped = []
    flips = [[1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
    for sub_pt in rotated:
        for flip in flips:
            new_pt = [sub_pt[i] * flip[i] for i in range(3)]
            flipped.append(tuple(new_pt))

    return flipped

testcase = set(all_pos((1,2,3)))
print(testcase)

def meta_pos(bunch):
    return [all_pos_2(pt) for pt in bunch]

def offset(universe, diff):
    res = []
    for pt in universe:
        res.append((pt[0] - diff[0], pt[1] - diff[1], pt[2] - diff[2]))
    return res




#remaining_scanners = [[(1,2,3), (2,3,4), (3,4,5)]]
#map = set([(0, 1, 2), (102, 103, 104), (101, 102, 103)])

CONFIRM_THRESHOLD = 12
import random

remaining_scanners = [([(0,0,0)], x) for x in scanners]

iii = 0
jjj = 0
universe_matrices = all_pos_2()
while len(remaining_scanners) > 1:
    # So we don't have to keep track of which scanner we're on
    
    jjj += 1
    if jjj >= len(remaining_scanners):
        jjj = 0
        iii += 1
    if iii >= len(remaining_scanners):
        iii = 0
        

    print(iii,jjj, len(remaining_scanners))
    if iii == jjj:
        continue

    map = remaining_scanners.pop(iii)
    if jjj > iii:
        next_scanner = remaining_scanners.pop(jjj-1)
    else:
        next_scanner = remaining_scanners.pop(jjj)

    map_foo, map = map
    next_foo, next_scanner = next_scanner

    
    num_universes = 24 # RSI is this always 24?

    searching = True
    for mat in universe_matrices:
        if not searching: break
        # Check a single universe
        points = [np.matmul(mat, x) for x in next_scanner]
        #print("")
        #print("Checking", points)

        
        for diff_point in points:
            if not searching: break
            for map_point in map:
                #print("what if point", diff_point)
                #print("is in map", map_point)

                diff = np.array(diff_point) - np.array(map_point)

                potential_points = offset(points, diff)
                #print("Potential points:", potential_points)
                intersection = map.intersection(set(potential_points))
                if len(intersection) >= CONFIRM_THRESHOLD:
                    print("FOUND OVERLAP at offset", diff)
                    map |= set(potential_points)
                    print("New map:", len(map))

                    # map scanner locations
                    for being_mapped in next_foo:
                        transformed_being_mapped = np.matmul(mat, being_mapped)
                        offset_being_mapped = transformed_being_mapped + diff
                        map_foo.append(offset_being_mapped)

                    remaining_scanners = [(map_foo, map)] + remaining_scanners

                    searching = False
                    break

    if searching == True:
        print("NO OVERLAP")
        remaining_scanners += [(map_foo, map), (next_foo, next_scanner)]

        
        #import pdb; pdb.set_trace()

def max_manhattan(ll):
    max_dist = 0
    for x in range(len(ll)):
        for y in range(len(ll)):
            dist = abs(ll[x][0] - ll[y][0]) + abs(ll[x][1] - ll[y][1]) + abs(ll[x][2] - ll[y][2])
            if dist > max_dist:
                max_dist = dist
    
    return max_dist
print(len(map))

print(max_manhattan(remaining_scanners[0][0]))

import pdb; pdb.set_trace()

#map = list(map)
#max_dist = 0
#
#for i in range(len(map)):
#    for j in range(len(map)):
#        if i == j:
#            continue
#            
#        a = map[i]
#        b = map[j]
#
#        dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
#        if dist > max_dist:
#            max_dist = dist
#
#print(max_dist)
#import pdb; pdb.set_trace()
