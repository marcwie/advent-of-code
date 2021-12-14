import numpy as np


def load_data(filename):

    with open(filename) as infile:

        data = infile.read().splitlines()
    
    data = np.array([list(row) for row in data]).astype(int)

    return data


def one_step(data):

    data = data + 1
    
    n_rows, n_cols = data.shape
    embedding = np.zeros((n_rows+2, n_cols+2)) - n_rows * n_cols
    embedding[1:n_rows+1, 1:n_cols+1] = data

    is_flashing = []

    while (embedding >= 10).any():
        indices = np.array(np.where(embedding >= 10)).T
        for row, col in indices:
            is_flashing.append([row, col]) 
            embedding[row, col] = 0
            for nb_row in (row-1, row, row+1):
                for nb_col in (col-1, col, col+1):
                    if [nb_row, nb_col] in is_flashing:
                        continue
                    embedding[nb_row, nb_col] += 1

    return embedding[1:n_rows+1, 1:n_cols+1]


def iterate(data, n_steps=10):
    
    n_flashes = 0
    for _ in range(n_steps):
        data = one_step(data)
        n_flashes += (data == 0).sum()
       
    return n_flashes


def find_sync(data):
   
    steps = 0
    while (data > 0).any():
        data = one_step(data)
        steps += 1
       
    return steps


def run():

    data = load_data(filename='data/day11/test')
    solution = iterate(data, n_steps=10)
    assert solution == 204
    solution = iterate(data, n_steps=100)
    assert solution == 1656

    data = load_data(filename='data/day11/input')
    solution = iterate(data, n_steps=100)
    print('Part1 solution:', solution)

    data = load_data(filename='data/day11/test')
    solution = find_sync(data)
    assert solution == 195

    data = load_data(filename='data/day11/input')
    solution = find_sync(data)
    print('Part2 solution:', solution)


if __name__ == '__main__':
    run()
