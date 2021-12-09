with open('puz3.txt') as f:
    lines = f.read().split('\n')


def try_num(x):
    try:
        return float(x)
    except:
        return x

one_counts = [0 for i in range(12)]
zero_counts = [0 for i in range(12)]

def most_common(l, pos):
    ones = 0
    zeros = 0
    for item in l:
        if item[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        return '0'
    if zeros > ones:
        return '1'
    return ' '

def answer(lis):
    for pos in range(len(lis[0])):
        new_list = []
        m = most_common(lis, pos)
        for i in lis:
            print(pos, m)
            if (m == ' ' and i[pos] == '0') or i[pos] == m:
                new_list.append(i)

        if len(new_list) == 1:
            return new_list[0]

        print(new_list)

        lis = new_list
    

print(most_common(lines, 0))
print(answer(lines))

#010010011001