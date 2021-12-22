players = (0, 0)



potential_rolls = []

for i in [1,2,3]:
    for j in [1,2,3]:
        for k in [1,2,3]:
            potential_rolls.append(i + j + k)

print(potential_rolls)


universes = [0, 0]
cache = {}

def turn(i, pos, players, foo):
    #print(i)
    possible_moves = []
    score = [0, 0]

    if (i, pos, players) in cache:
        #print("cached", cache[(i, pos, players)])
        return cache[(i, pos, players)]

    for roll in potential_rolls:
        new_pos = list(pos)
        new_players = list(players)
        new_pos[i] += roll

        if new_pos[i] > 10:
            new_pos[i] -= 10
        new_players[i] += new_pos[i]

        #print(foo,((i+1)%2, tuple(new_pos), tuple(new_players)))

        if new_players[i] >= 21:
            score[i] += 1
            #print(foo, "scored 1")
        else:
            #print(foo, "not scored")
            sub_scores = turn((i+1)%2, tuple(new_pos), tuple(new_players), foo+' ')
            score[0] += sub_scores[0]
            score[1] += sub_scores[1]

    #import pdb; pdb.set_trace()
   
    cache[(i, pos, players)] = score
    return score



print(turn(0, (1, 3), (0, 0), ''))