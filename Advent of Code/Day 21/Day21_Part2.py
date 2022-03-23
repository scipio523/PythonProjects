from itertools import product
from collections import Counter
from functools import lru_cache

p1_pos = 7
p2_pos = 1
position = {1:p1_pos-1, 2:p2_pos-1}
# 1 is being subtracted so we can safely take the modulo 10 of the position
# (therefore 1 is going to be added to the score for each move)

# All combinations of 3 dices that yields the same sum
# (counts how many times a specific sum repeats among all possible rolls)
dice_sums = Counter(sum(rolls) for rolls in product((1,2,3), repeat=3))

@lru_cache(maxsize=None)    # <-- Cache the results of the function
                            # (when the function is called with the same parameters, it returns the same result without being executed)
def dirac_dice(p1_pos, p2_pos, p1_score=0, p2_score=0):
    global dice_sums
    
    # Return the win count when a player reaches 21 points
    if p1_score >= 21: return (1, 0)
    if p2_score >= 21: return (0, 1)

    # Cumulative amount of wins for each player
    p1_wins_total = 0
    p2_wins_total = 0

    # Iterate over all possible rolls in a turn
    for roll, amount in dice_sums.items():
        
        # Move the player and increment their score
        p1_pos_new = (p1_pos + roll) % 10
        p1_score_new = p1_score + p1_pos_new + 1

        # Pass the turn to the other player
        p2_wins, p1_wins = dirac_dice(p2_pos, p1_pos_new, p2_score, p1_score_new)

        # Increment the win counter by the results multiplied by the amount of times the roll repeats
        p1_wins_total += p1_wins * amount
        p2_wins_total += p2_wins * amount
    
    # Returns the final tally of victories
    return (p1_wins_total, p2_wins_total)

max_victories = max(
    dirac_dice(
        p1_pos = position[1],
        p2_pos = position[2]
    )
)

print(f"Part 2: {max_victories}")