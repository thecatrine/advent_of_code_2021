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
    return [all_pos(pt) for pt in bunch]

def offset(universe, diff):
    res = []
    for pt in universe:
        res.append((pt[0] - diff[0], pt[1] - diff[1], pt[2] - diff[2]))
    return res




#remaining_scanners = [[(1,2,3), (2,3,4), (3,4,5)]]
#map = set([(0, 1, 2), (102, 103, 104), (101, 102, 103)])

CONFIRM_THRESHOLD = 12
import random

remaining_scanners = [scanners[x] for x in [0, 1, 4, 3, 2]]

while len(remaining_scanners) > 1:
    # So we don't have to keep track of which scanner we're on
    #random.shuffle(remaining_scanners)

    map = remaining_scanners.pop(0)
    next_scanner = remaining_scanners.pop(0)

    all_universes = meta_pos(next_scanner)
    num_universes = 24 # RSI is this always 24?

    searching = True
    for i in range(num_universes):
        if not searching: break
        # Check a single universe
        points = [all_universes[x][i] for x in range(len(all_universes))]
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
                    remaining_scanners = [map] + remaining_scanners

                    searching = False
                    break

    if searching == True:
        print("NO OVERLAP")
        remaining_scanners += [map, next_scanner]

        
        #import pdb; pdb.set_trace()

print(len(map))

