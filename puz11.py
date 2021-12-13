with open('puz11.txt') as f:
    lines = f.read().split('\n')

X, Y = len(lines), len(lines[0])        

map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

def breadth(map, spots):
    while len(spots) > 0:
        spot = spots.pop()
        pass



def step(map):
    flashes = 0
    for y in range(Y):
        for x in range(X):
            map[(y,x)] += 1
    
    flashed = True
    flashed_points = set()
    while flashed:
        flashed = False
        for (y,x) in map.keys():
            if (y,x) not in flashed_points and map.get((y,x), 0) > 9:
                flashed = True
                flashes += 1
                
                for spot in [(y+1, x), (y-1, x), (y, x+1), (y, x-1), (y+1, x+1), (y-1, x+1), (y+1, x-1), (y-1, x-1)]:
                    if spot in map:
                        map[spot] += 1

                flashed_points.add((y,x))
                print(flashed_points)
                
                print("flash", y, x)

    for x in flashed_points:
        map[x] = 0

    for y in range(Y):
        line = ""
        for x in range(X):
            line += str(map.get((y,x), 0))
        print(line)
    print()

    return flashes


flashes = 0
i = 0
while True:
    i+= 1
    flashes = step(map)
    if flashes == 100:
        print(i)
        break
    
