with open('puz6.txt') as f:
    lines = f.read().split('\n')


counts = dict([[x, 0] for x in range(9)])
print(counts)
for x in lines[0].split(','):
    num = int(x)
    counts.setdefault(num, 0)
    counts[num] += 1

print(counts)

new_counts = dict([[x, 0] for x in range(9)])
for i in range(256):
    new = counts[0]
    for i in range(0, 9):
        num = counts.get(i+1, 0)
        new_counts[i] = num

    new_counts[6] += new
    new_counts[8] += new

    counts = new_counts.copy()
    print(new_counts)

print(sum(counts.values()))