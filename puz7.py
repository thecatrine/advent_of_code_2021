with open('puz7.txt') as f:
    lines = f.read().split('\n')


pos = {}

print(lines[0])

def positions(l):
    pos = {}
    for x in l.split(','):
        num = int(x)
        
        pos.setdefault(num, 0)
        pos[num] += 1
    
    return pos, min(pos.keys()), max(pos.keys())
 

pos, a, b = positions(lines[0])

print(pos, a, b)

def costf(x):
    return sum(range(x, 0, -1))

costs = {}

for i in range(a, b+1):
    cost = 0
    for k, v in pos.items():
        cost += v*costf(abs(i-k))
    costs[i] = cost

print(min(costs.values()))