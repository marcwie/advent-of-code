def load_data(filename):
    
    with open(filename) as infile:
        data = infile.read().splitlines()
    data = [int(value) for value in data]

    return data


def count_increments(data, window_size=1):
    data = sliding_window(data, window_size=window_size)
    return sum([data[i] < data[i+1] for i in range(len(data)-1)])


def sliding_window(data, window_size):
    n_data = len(data)
    return [sum(data[i:i+window_size]) for i in range(n_data + 1 -window_size)]


def run():
    data = load_data('data/day01/test')
    solution = count_increments(data)
    assert solution == 7

    data = load_data('data/day01/input')
    solution = count_increments(data)
    print('Part1 Solution:', solution)
    assert solution == 1184

    data = load_data('data/day01/test')
    solution = count_increments(data, window_size=3)
    assert solution == 5

    data = load_data('data/day01/input')
    solution = count_increments(data, window_size=3)
    print('Part2 Solution:', solution)
    assert solution == 1158


if __name__ == '__main__':
    run()
