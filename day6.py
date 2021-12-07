import numpy as np


def load_data(filename='data/day6/test'):
    
    with open(filename) as infile:
        data = infile.readline().split(',')

    data = np.array(data).astype(int)

    return data


def one_update(state):
    
    n_new = state[0]
    state = state[1:]
    state[6] += n_new
    state.append(n_new)

    return state

def run():

    state = load_data(filename='data/day6/input')
    state = [(state == i).sum() for i in range(9)]
    for _ in range(80):
        state = one_update(state=state)
    
    print('Part1 Solution:', sum(state))

    state = load_data(filename='data/day6/input')
    state = [(state == i).sum() for i in range(9)]
    for _ in range(256):
        state = one_update(state=state)
    
    print('Part2 Solution:', sum(state))


if __name__ == '__main__':
    run()
