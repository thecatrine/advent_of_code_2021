with open('puz12.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

map = {}

for line in lines:
    a, b = line.split('-')

    map.setdefault(a, []).append(b)
    map.setdefault(b, []).append(a)

def canvisit(hist, a):
    if a == 'start':
        return False

    if a.lower() != a:
        return True
    
    counts = {}

    if a not in hist:
        return True

    for h in hist:
        if h.lower() == h:
            counts.setdefault(h, 0)
            counts[h] += 1
    
    if max(counts.values()) > 1:
        return False

    return True
    

def paths(visited):
    pos = map[visited[-1]]
    #print(f"from {cur}: {pos}")

    if visited[-1] == "end":
        print(visited)
        return 1

    tot = 0

    for p in pos:
        if canvisit(visited, p):
            print(visited, pos, visited[-1], p)
            new_visited = visited.copy()
            new_visited.append(p)

            tot += paths(new_visited)

    return tot



print(paths(["start"]))
