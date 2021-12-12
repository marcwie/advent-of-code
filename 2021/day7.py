import numpy as np


def load_data(filename='data/day7/test'):
    
    with open(filename) as infile:
        data = infile.readline().split(',')

    data = np.array(data).astype(int)

    return data


def weighted_consumption(data):
    
    min_x = data.min()
    max_x = data.max()
    
    consumptions = []
    for final_x in range(min_x, max_x+1):
        distance = np.abs(data - final_x)
        consumptions.append((.5 * distance * (distance + 1)).sum())
    
    return int(min(consumptions))


def consumption(data):
    return int(np.abs(data - np.median(data)).sum())


def run():
    
    data = load_data('data/day7/test')
    solution = consumption(data) 
    assert solution == 37

    solution = weighted_consumption(data)
    assert solution == 168

    data = load_data('data/day7/input')
    solution = consumption(data) 
    print('Part1 solution:', solution)

    solution = weighted_consumption(data)
    print('Part2 solution:', solution)


if __name__ == '__main__':
    run()
