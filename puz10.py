with open('puz10.txt') as f:
    lines = f.read().split('\n')

X, Y = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])

def breadth(map, spots):
    while len(spots) > 0:
        spot = spots.pop()
        pass


m = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
def is_corrupt(l):
    brackets = []
    for char in l:
        if char in ['(', '[', '{', '<']:
            brackets.append(char)
        if char in [')', ']', '}', '>']:
            if len(brackets) == 0 or brackets.pop() != m[char]:
                return True, []

    return False, brackets


scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

tot = []
for l in lines:
    corr, b = is_corrupt(l)
    if not corr:
        score = 0
        print(b)
        for x in reversed(b):
            score *= 5
            score += scores[x]
        tot.append(score)

print(tot)
print(sorted(tot))

while len(tot) > 1:
    tot.pop(0)
    tot.pop(-1)

print(tot)