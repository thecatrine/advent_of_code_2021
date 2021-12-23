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
        scanners[-1].append(np.array([x, y, z]))


for i in range(len(scanners)):
    scanners[i] = np.array(scanners[i])


map = []

# assume scanner 0 has the right coordinate system
for pt in scanners[0]:
    map.append(tuple(pt))


def all_pos(pt):
    rotated = []
    swaps = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
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

def meta_pos(bunch):
    return [all_pos(pt) for pt in bunch]

def offset(universe, diff):
    res = []
    for pt in universe:
        res.append((pt[0] - diff[0], pt[1] - diff[1], pt[2] - diff[2]))
    return res


remaining_scanners = scanners

#remaining_scanners = [[(1,2,3), (2,3,4), (3,4,5)]]
#map = set([(0, 1, 2), (102, 103, 104), (101, 102, 103)])

CONFIRM_THRESHOLD = 12

while len(remaining_scanners) > 0:
    map = remaining_scanners.pop()
    next_scanner = remaining_scanners.pop()

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
                    print("FOUND OVERLAP")
                    searching = False
                    for found_pt in potential_points:
                        map.add(found_pt)
                    break

    if searching == True:
        print("NO OVERLAP")
        remaining_scanners = [next_scanner] + remaining_scanners

        
        #import pdb; pdb.set_trace()

print(len(map))

