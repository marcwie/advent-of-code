def load_data(filename='data/day06/test'):
    
    with open(filename) as infile:
        data = infile.read().replace('\n', '').split(',')
    data = [int(n) for n in data]

    return data


def one_update(state):
    
    n_new = state[0]
    state = state[1:]
    state[6] += n_new
    state.append(n_new)

    return state


def solve(state, n_runs):

    state = [sum([s == i for s in state]) for i in range(9)]
    for _ in range(n_runs):
        state = one_update(state=state)
    
    return sum(state)


def run():
    
    state = load_data(filename='data/day06/test')
    solution = solve(state=state, n_runs=80) 
    assert solution == 5934

    solution = solve(state=state, n_runs=256) 
    assert solution == 26984457539

    state = load_data(filename='data/day06/input')
    solution = solve(state=state, n_runs=80) 
    print('Part1 solution:', solution)
    assert solution == 346063

    solution = solve(state=state, n_runs=256) 
    print('Part2 solution:', solution)
    assert solution == 1572358335990


if __name__ == '__main__':
    run()
