with open('puz14.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

X, Y = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

foo = lines[0]

map = {}

for line in lines[1:]:
    a, b = line.split(' -> ')

    map[a] = b

print(map)

pairs = {}

for i in range(len(foo)-1):
    item = foo[i:i+2]
    pairs.setdefault(item, 0)
    pairs[item] += 1

counts = {foo[-1]: 1}

for q in range(40):
    new_pairs = pairs.copy()
    print(new_pairs)
    print('---')
    for k, v in pairs.items():
        if v == 0:
            continue
        #print(k)
        n = map[k]
        a = k[0] + n
        b = n + k[1]

        print(k, "->", a, b)

        new_pairs[k] -= v
        new_pairs.setdefault(a, 0)
        new_pairs[a] += v
        new_pairs.setdefault(b, 0)
        new_pairs[b] += v

    pairs = new_pairs



for k, v in pairs.items():
    counts.setdefault(k[0], 0)
    counts.setdefault(k[1], 0)

    counts[k[0]] += v

print(counts, max(counts.values())-min(counts.values()))