def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    return [[int(entry) for entry in list(row)] for row in data] 


def one_step(data):
    
    data = [[d + 1 for d in row] for row in data]

    n_rows, n_cols = len(data), len(data[0])
    embedding = [[-n_rows * n_cols] * (n_cols + 2)]
    for row in data:
        embedding.append([-n_rows * n_cols] + row + [-n_rows * n_cols])
    embedding.append([-n_rows * n_cols] * (n_cols + 2))
    
    is_flashing = []
    idxi, idxj = range(1, n_rows+1), range(1, n_cols+1)

    while sum([d >= 10 for row in embedding for d in row]):
        indices = [[i, j] for i in idxi for j in idxj if embedding[i][j] >= 10]
        for row, col in indices:
            is_flashing.append([row, col]) 
            embedding[row][col] = 0
            for nb_row in (row-1, row, row+1):
                for nb_col in (col-1, col, col+1):
                    if [nb_row, nb_col] in is_flashing:
                        continue
                    embedding[nb_row][nb_col] += 1

    return [row[1:-1] for row in embedding[1:-1]]


def iterate(data, n_steps=10):
    
    n_flashes = 0
    for _ in range(n_steps):
        data = one_step(data)
        n_flashes += sum([d == 0 for row in data for d in row])
       
    return n_flashes


def find_sync(data):
   
    steps = 0
    while sum([d > 0 for row in data for d in row]):
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
    assert solution == 1652

    data = load_data(filename='data/day11/test')
    solution = find_sync(data)
    assert solution == 195

    data = load_data(filename='data/day11/input')
    solution = find_sync(data)
    print('Part2 solution:', solution)
    assert solution == 220


if __name__ == '__main__':
    run()
