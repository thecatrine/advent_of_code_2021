with open('puz24.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

Y, X = len(lines), len(lines[0])        

instructions = []

for line in lines:
    a = []
    blah = line.split(' ')
    for x in blah:
        try:
            b = int(x)
            a.append(b)
        except:
            a.append(x)
    instructions.append(a)

import math

def convert(instructions):
    program = """
int test_num(int* num) {
    int w = 0; int x = 0; int y = 0; int z = 0;
"""

    for instruction in instructions:
        com, rest = instruction[0], instruction[1:]

        if com == 'inp':
            program += f'    {rest[0]} = *num;num++;\n'
        if com == 'add':
            program += f'    {rest[0]} += {rest[1]};\n'
        if com == 'mul':
            program += f'    {rest[0]} *= {rest[1]};\n'
        if com == 'div':
            program += f'    {rest[0]} /= {rest[1]};\n'
        if com == 'mod':
            program += f'    {rest[0]} = {rest[0]} % {rest[1]};\n'
        if com == 'eql':
            program += f'    if ({rest[0]} == {rest[1]}) ' + '{' + f'{rest[0]} = 1;' + '} else {' + f'{rest[0]} = 0;' + '}\n'
    
    program += '    if (z == 0) {return 1;} else {return 0;}\n}'
    return program

print(convert(instructions))