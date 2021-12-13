
with open('puz9.txt') as f:
    lines = f.read().split('\n')

X, Y = len(lines), len(lines[0])        

map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

def count(map, spots, count):
    while spots:
        y,x = spots.pop(); map[(y,x)] = 9; count += 1
        [spots.add(new_spot) for new_spot in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)] if map.get(new_spot, 9) != 9]
    return count

a = sorted(
    [count(map, set([(y,x)]), 0) for y in range(Y) for x in range(X) if map[(y,x)] != 9]
)[-3:]

print(a[0]*a[1]*a[2])
