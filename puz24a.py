steps = [
    [False, 13, 15],
    [False, 13, 16],
    [False, 10, 4],
    [False, 15, 14],
    [True, -8, 1],
    [True, -10, 5],
    [False, 11, 1],
    [True, -3, 3],
    [False, 14, 3],
    [True, -4, 7],
    [False, 14, 5],
    [True, -5, 13],
    [True, -8, 3],
    [True, -11, 10],
]

max_length = 0

def test(old_num="", old_z=[], adds=6, i=0):
    global max_length

    if i == len(steps):
        #print("NO MORE STEPS")
        if len(old_z) == 0:
            print("DONE!", old_num)
        else:
            print("CLOSE :( ", old_num)
        return
    step = steps[i]
    zz = old_z.copy()

    de = False
    if i > max_length:
        print(old_num, i)
        print(old_z)
        max_length = i
        de = True
        

    if len(zz) == 0:
        if i == 0:
            x = 0
        else:
            print(old_num)
            raise Exception("STOP")
    else:
        if step[0]:
            x = zz.pop()
        else:
            x = zz[-1]
    
    #print(str(i), ('  '*i)[len(str(i)):], step, adds)
    x = x + step[1] # Add number from step
    #print(str(i), ('  '*i)[len(str(i)):],old_num, zz)
    #print('')
    # if x != w: z.append(step[2])

    free_nums = []
    add_nums = []
    for w in [1,2,3,4,5,6,7,8,9]:


        if x != w and adds > 0:
            add_nums.append(w)
        elif x == w:
            free_nums.append(w)

    if de:
        pass
#        import pdb; pdb.set_trace()
    
    for free in free_nums:
        num = old_num + str(free)
        z = zz.copy()
        test(num, z, adds, i + 1)
    
    for add in add_nums:
        num = old_num + str(add)
        z = zz.copy()
        z.append(add + step[2])

        test(num, z, adds - 1, i + 1)


test("", [], adds=7, i=0)