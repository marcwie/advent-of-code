import numpy as np


def load_data(filename='data/day9/test'):
    
    with open(filename) as infile:
    
        data = infile.read().splitlines()
    
    data = np.array([list(row) for row in data]).astype(int)
    
    return data


def get_risk_score(heights):

    risk_score = 0
    n_rows, n_cols = heights.shape
    max_height = heights.max()

    embedding = np.ones((n_rows+2, n_cols+2), dtype=int) * 10 * max_height
    embedding[1:n_rows+1, 1:n_cols+1] = heights
    
    for row in range(1, n_rows+1):
        for col in range(1, n_cols+1):
            pos = embedding[row, col]
            indices = [[row-1, row, row, row+1], [col, col-1, col+1, col]]
            if np.all(embedding[row, col] < embedding[tuple(indices)]):
                risk_score += embedding[row, col] + 1
    
    return risk_score


def find_basin(indices):
    
    basin = [indices[0]]
    candidates = indices[1:]

    while True:
        new_indices = [] 

        for row, col in basin:
            nbs = [[row, col+1], [row, col-1], [row+1, col], [row-1, col]]
            for nb in nbs:
                if nb in candidates:
                    new_indices.append(nb)
                    candidates.remove(nb)

        if not len(new_indices):
            break
        
        for index in new_indices:
            basin.append(index)
    
    return basin, candidates
     
        
def find_basins(heights):

    indices = np.array(np.where(heights < 9)).T.tolist()
    
    basins = []
    while len(indices):
        basin, indices = find_basin(indices)    
        basins.append(basin)
    
    basins = [len(basin) for basin in basins]
    basins.sort()
    n1, n2, n3 = basins[-3:]
    
    return n1 * n2 * n3


def part1():
    
    data = load_data(filename='data/day9/test')
    solution = get_risk_score(heights=data)
    assert solution == 15

    data = load_data(filename='data/day9/input')
    solution = get_risk_score(heights=data)
    print('Part1 solution:', solution)


def part2():
    data = load_data(filename='data/day9/test')
    solution = find_basins(heights=data)
    assert solution == 1134

    data = load_data(filename='data/day9/input')
    solution = find_basins(heights=data)
    print('Part2 solution:', solution) 


if __name__ == '__main__':
    part1()
    part2()
