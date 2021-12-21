class Die():

    def __init__(self):
    
        self.steps = 0
        self.current_roll = 1

    def roll(self):

        rolls = [self.current_roll + i for i in range(3)]
        rolls = [roll if roll <= 100 else roll - 100 for roll in rolls]
        self.current_roll = rolls[-1] + 1
        self.steps += 3

        return sum(rolls)


def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()

    pos1, pos2 = [int(row.split(': ')[1]) for row in data]
    return pos1, pos2


def play(pos1, pos2):

    die = Die()
    score1, score2 = 0, 0
    while score1 < 1000 and score2 < 1000:
        pos1, score1 = compute_score(pos1+die.roll(), score1)
        if score1 < 1000:
            pos2, score2 = compute_score(pos2+die.roll(), score2)

    return die.steps * min([score1, score2])


def compute_score(pos, score):

    while pos > 10:
       pos = pos - 10
    score = score + pos

    return pos, score


def count(counter, state, times):
    
    if state in counter.keys():
        counter[state] += times
    else:
        counter[state] = times
    return counter


def play_dirac(pos1, pos2):
    
    rolls = [i+j+k+3 for i in range(3) for j in range(3) for k in range(3)]
    dice = {}
    for roll in rolls:
        dice = count(dice, roll, 1)
   
    win = [0, 0]
    states = {((pos1, 0), (pos2, 0)): 1} 
    player = 0

    while len(states):
        
        next_states = {}
        for state, n in states.items():
            pos, score = state[player]
            for value, r in dice.items():
                _pos, _score = compute_score(pos+value, score) 
                if _score >= 21:
                    win[player] += r * n
                    continue
                if player == 0:
                    next_state = ((_pos, _score), state[1])
                else:
                    next_state = (state[0], (_pos, _score))
                next_states = count(next_states, next_state, r * n)

        states = next_states
        player = (player + 1) % 2

    return max(win)


def run():

    pos1, pos2 = load_data('data/day21/test')
    solution = play(pos1, pos2)
    assert solution == 739785

    pos1, pos2 = load_data('data/day21/input')
    solution = play(pos1, pos2)
    print('Part1 solution:', solution)
    
    pos1, pos2 = load_data('data/day21/test')
    solution = play_dirac(pos1, pos2)
    assert solution == 444356092776315
    
    pos1, pos2 = load_data('data/day21/input')
    solution = play_dirac(pos1, pos2)
    print('Part2 solution:', solution)
    assert solution == 146854918035875
 

if __name__ == '__main__':
    run()
