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


def solve(state, n_runs):

    state = [(state == i).sum() for i in range(9)]
    for _ in range(n_runs):
        state = one_update(state=state)
    
    return sum(state)

def run():
    
    state = load_data(filename='data/day6/test')
    solution = solve(state=state, n_runs=80) 
    assert solution == 5934

    solution = solve(state=state, n_runs=256) 
    assert solution == 26984457539

    state = load_data(filename='data/day6/input')
    solution = solve(state=state, n_runs=80) 
    print('Part1 solution:', solution)

    solution = solve(state=state, n_runs=256) 
    print('Part2 solution:', solution)


if __name__ == '__main__':
    run()
