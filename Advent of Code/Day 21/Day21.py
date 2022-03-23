# Test Input:  Player 1 = 4, Player 2 = 8
# My Input: Player 1 = 7, Player 2 = 1

p1_pos = 7
p2_pos = 1
p1_score = 0
p2_score = 0
roll = 0
roll_count = 0
turn = 'p1'
while True:
    roll += 3
    roll_count += 3
    if turn == 'p1':
        p1_pos = (p1_pos + roll*3 - 3) % 10
        if p1_pos == 0: p1_pos = 10
        p1_score += p1_pos
        turn = 'p2'
    else:
        p2_pos = (p2_pos + roll*3 - 3) % 10
        if p2_pos == 0: p2_pos = 10
        p2_score += p2_pos
        turn = 'p1'
    if roll > 100:
        roll = roll % 100
    if p1_score >= 1000:
        result = p2_score * roll_count
        break
    elif p2_score >= 1000:
        result = p2_score * roll_count
        break
print(result)