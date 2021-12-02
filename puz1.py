with open('puz1.txy.txt') as f:
    lines = f.read().split('\n')


windows = []

j=0
for i in range(0, len(lines)-2):
    windows.append(int(lines[i])+int(lines[i+1])+int(lines[i+2]))

print(len(windows))
z = 0
x = windows[0]

for i in windows[1:]:
    if i > x:
        z += 1
    x = i

print(z)