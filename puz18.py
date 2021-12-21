with open('puz18.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

#map = dict([[(y,x), int(lines[y][x])] for y in range(Y) for x in range(X)])


def col(x):
    return ''.join([str(y) for y in x])

def parse(term):
    depth = 0
    parsing = ""

    item = []

    for i in term:
        if i in '0123456789':
            parsing += i
        else:
            if parsing != "":
                item.append(int(parsing))
                parsing = ""
            
            item.append(i)

    for x in range(len(item)):
        i = item[x]
        if i == '[':
            depth += 1
        elif i == ']':
            depth -= 1

        if x+2 < len(item) and \
            isinstance(i, int) and \
            isinstance(item[x+2], int) and \
            depth > 4:
            a = item[x]
            b = item[x+2]

            for j in range(x-1, 0, -1):
                if isinstance(item[j], int):
                    item[j] += a
                    break
            for j in range(x+3, len(item)):
                if isinstance(item[j], int):
                    item[j] += b
                    break
            
            print(col(item[:x-1]),"-----",col(item[x+4:]))
            item = item[:x-1] + [0] + item[x+4:]
            return ''.join([str(x) for x in item]), True

    for x in range(len(item)):
        if isinstance(item[x], int) and item[x] > 9:
            import math
            fooa = math.floor(item[x] / 2)
            foob = math.ceil(item[x] / 2)

            item = item[:x] + ['[', fooa, ',', foob, ']'] + item[x+1:]
            return ''.join([str(x) for x in item]), True


    return ''.join([str(x) for x in item]), False


def add(a, b):
    return '[' + a + ',' + b + ']'

def reduce(foo):
    go = True
    while go:
        foo, go = parse(foo)
        print(foo, go)

    return foo


def mag(x):
    if isinstance(x, int):
        return x

    a, b = x
    return 3*mag(a) + 2*mag(b)



#a = None
#for b in lines:
#    print("line ", b)
#    if a == None:
#        a = b
#    else:
#        a = add(a, b)
#        print("add ", a)
#        a = reduce(a)

#print(a)
#print(mag(eval(a)))

m = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            added = add(lines[i], lines[j])
            added = reduce(added)
            #print(added)
            mmm = mag(eval(added))
            if mmm > m:
                m = mmm
                print(i, j, mmm)

print(m)