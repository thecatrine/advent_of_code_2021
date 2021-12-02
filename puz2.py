with open('puz2.txt') as f:
    lines = f.read().split('\n')


def try_num(x):
    try:
        return float(x)
    except:
        return x

sub_lines = [[try_num(x) for x in line.split()] for line in lines if line.strip() != '']

x = 0
y = 0
aim = 0

for line in sub_lines:
    print(line)
    dir, num = line
    if dir == "forward":
        x += num
        y += aim * num
    if dir == "down":
        aim += num
    if dir == "up":
        aim -= num

print(x*y)