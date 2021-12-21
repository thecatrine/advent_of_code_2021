with open('puz16.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

X, Y = len(lines), len(lines[0])        

# packet version 3 bits

versions = 0

hexmap = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111',
}

def hex_to_binary(hex):
    binary = ''
    for a in hex.lower():
        binary += hexmap[a]

    return binary

def parse(hex=None, bbb=None):
    global versions
    if hex is not None:
        binary_string = hex_to_binary(hex)
    else:
        binary_string = bbb

    if len(binary_string) < 6: return '', None

    
    print()
    print()
    print("binary_string", binary_string)

    version = int(binary_string[0:3], 2)
    print("version               ", version)
    versions += version
    type = int(binary_string[3:6], 2)

    rest = binary_string[6:]
    print(rest)

    value = None
    if type == 4:
        go = 1

        bits = ""
        j = 0
        i = 0
        while go:
            start = i * 5
            bits += rest[start+1:start+5]
            j = start+5
            i += 1
            if rest[start] == '0':
                go = 0

        literal = int(bits, 2)
        print("literal", literal)
        value = literal
        rest = rest[j:]
    else:
        # operators
        sub_values = []
        if rest[0] == '0':
            
            # 15 bit number
            total_len = int(rest[1:16], 2)
            print(f"len {total_len}")

            sub_rest = rest[16:16+total_len]
            while sub_rest != '':
                sub_rest, sub_val = parse(bbb=sub_rest)
                sub_values.append(sub_val)

            rest = rest[16+total_len:]
        else:
            total_num = int(rest[1:12], 2)

            rest = rest[12:]
            for i in range(total_num):
                rest, sub_value = parse(bbb=rest)
                sub_values.append(sub_value)
        
        if type == 0:
            value = sum(sub_values)
        elif type == 1:
            value = 1
            for sub_value in sub_values:
                value *= sub_value
        elif type == 2:
            value = min(sub_values)
        elif type == 3:
            value = max(sub_values)
        elif type == 5:
            if sub_values[0] > sub_values[1]:
                value = 1
            else:
                value = 0
        elif type == 6:
            if sub_values[0] < sub_values[1]:
                value = 1
            else:
                value = 0
        elif type == 7:
            if sub_values[0] == sub_values[1]:
                value = 1
            else:
                value = 0

    return rest, value
        

rest = lines[0]
print("res ", parse(lines[0]))
print("versions", versions)