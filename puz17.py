with open('puz17.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

print(X, Y, lines[0])

xx = (211, 232)
yy = (-124, -69)

def height(xv, yv):
    x = 0
    y = 0
    height = 0

    while 1:
        if y > height:
            height = y

        x += xv
        y += yv

        if xv > 0: xv -= 1
        elif xv < 0: xv += 1

        yv -= 1

        if x >= xx[0] and x <= xx[1] and y >= yy[0] and y <= yy[1]:
            return height
        if y < yy[0] or x > xx[1]:
            return None


max_height = 0
xxx = 0

for x in range(0, xx[1]*2):
    for y in range(-1000, 2000):
        new_height = height(x, y)

        if new_height is not None:
            xxx += 1
        if new_height and new_height > max_height:
            max_height = new_height

print(max_height, xxx)