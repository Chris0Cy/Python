# grid-m4.py

NUM_STATES = 50
# It's actually still a 5x5 grid, but we use the first half
# to number states before the treasure is taken, and the
# second half (25..49) to number states after treasure is taken.

# To be specific, if the treasure is in position 11, when you enter
# that position (for example going east from 10) you actually
# transition to state 36 (11+25) because now the treasure is consumed.
# There's no way to get back to states < 25.

# Also the goal state gets duplicated. It's at position 12, but that
# state# represents not having the treasure. So if you go to 12 you'd
# end the game with no reward. What we really want is to get to state
# 37 (12+25), that's where we get the reward for ending the game.

# grid01.py -- figure 3.5 from RL book.
ACTIONS = ['N', 'S', 'E', 'W','P']
GAMMA = 0.9                     # future discount rate

def step(state, action):  # returns (newState, reward)
    if state == 1:        # teleport "A"
        return (21, 10)
    if state == 32:  # winning conditions
        return (0,0)
    if state == 3:              # teleport "B"
        return (13, 5)
    if action == 'W' and state%5 == 0: # left column
        return (state, -1)
    if action == 'N' and state < 5: # top row
        return (state, -1)
    if action == 'E' and state%5 == 4: # right column
        return (state, -1)
    if action == 'S' and state >= 20: # bottom row
        return (state, -1)
    # The rest are legit actions with zero reward/penalty.
    if action == 'S':
        return (state+5, 0)
    if action == 'N':
        return (state-5, 0)
    if action == 'E':
        return (state+1, 0)
    if action == 'W':
        return (state-1, 0)
    assert False #impossible?

def value_function_equiprobable_one_pass(estimates):
    for st in range(NUM_STATES):
        stateN, rewardN = step(st, 'N')
        stateS, rewardS = step(st, 'S')
        stateE, rewardE = step(st, 'E')
        stateW, rewardW = step(st, 'W')
        avg = (rewardN + GAMMA * estimates[stateN] +
               rewardS + GAMMA * estimates[stateS] +
               rewardE + GAMMA * estimates[stateE] +
               rewardW + GAMMA * estimates[stateW] ) /4
       # print(avg)
        estimates[st] = avg

if __name__ == "__main__":
    import numpy as np
    est = np.zeros([NUM_STATES])
    for _ in range(100):        # number of iterations
        value_function_equiprobable_one_pass(est)
    print(est)
