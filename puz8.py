
with open('puz8.txt') as f:
    lines = f.read().split('\n')


sum = 0
for line in lines:
    blah = [x for x in line.split('|')[1].split(' ') if x != '']
    for i in blah:
        if len(i) in [7, 3, 2, 4]:
            sum += 1

def parse(l):
    inp = [x for x in l.split('|')[0].split(' ') if x != '']
    res = [x for x in l.split('|')[1].split(' ') if x != '']
    return inp, res

# 0 -> 6
# 9 -> 6
# 6 -> 6

# 1 -> 2

# 2 -> 5
# 3 -> 5
# 5 -> 5

# 4 -> 4

# 7 -> 3

# 8 -> 7


sets = {
    3: "bdeg",
    7: "",
    2: "abdeg",
    4: "aeg",
}

multi = {
    5: ['bf', 'be', 'ce'],
    6: ['d', 'c', 'e'],
}

def number_from_set(s):
    if s == set(['a','b','c','e','f','g']):
        return 0
    if s == set(['c','f']):
        return 1
    if s == set(['a','c','d','e','g']):
        return 2
    if s == set(['a','c','d','f','g']):
        return 3
    if s == set(['b','c','d','f']):
        return 4
    if s == set(['a','b','d','f','g']):
        return 5
    if s == set(['a','b','d','e','f','g']):
        return 6
    if s == set(['a','c','f']):
        return 7
    if s == set(['a','b','c','d','e','f','g']):
        return 8
    if s == set(['a','b','c','d','f', 'g']):
        return 9
    raise Exception("No number for set", s)

def calc(inp, res):
    pos = {}
    for let in ['a', 'b','c','d','e','f','g']:
        pos[let] = set(['a', 'b','c','d','e','f','g'])
    
    inall5 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    inall6 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    for i in inp:
        if len(i) in sets.keys():
            imposs_set = set([x for x in sets[len(i)]])
            for item in i:
                print(f"{item} cant be in {imposs_set}")
                pos[item] = pos[item] - imposs_set

        if len(i) == 5:
            inall5 = inall5.intersection( set([x for x in i]) )
            print("inall5", inall5)

        if len(i) == 6:
            inall6 = inall6.intersection( set([x for x in i]) )
            print("inall6", inall6)

    # can't be in any because they were in intersections
    for i in inall6:
        pos[i] = pos[i] - set(['c','e','d'])

    for i in inall5:
        pos[i] = pos[i] - set(['c','b','e','f'])
    
    go = True
    while go:
        go = False
        for i in 'abcdefg':
            if len(pos[i]) == 1:
                for j in 'abcdefg':
                    if i != j:
                        pos[j] = pos[j] - pos[i]
            else:
                go = True

    print(pos)

    num = ''
    for item in res:
        item_set = set([list(pos[x])[0] for x in item])
        n = number_from_set(item_set)
        num += str(n)
    
    return int(num)
            
sum = 0
for line in lines:
    #test = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    a, b = parse(line)
    print(a,b)
    sum += calc(a, b)
print(sum)