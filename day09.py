def load_data(filename='data/day09/test'):
    
    with open(filename) as infile:
        data = infile.read().splitlines()
    return [[int(entry) for entry in list(row)] for row in data] 


def get_risk_score(heights):

    risk_score = 0
    n_rows, n_cols = len(heights), len(heights[0])
    max_height = max([h for row in heights for h in row])

    embedding = [[max_height] * (n_cols + 2)]
    for height in heights:
        embedding.append([max_height] + height + [max_height])
    embedding.append([max_height] * (n_cols + 2))

    for row in range(1, n_rows+1):
        for col in range(1, n_cols+1):
            pos = embedding[row][col]
            indices = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
            if sum([pos < embedding[i][j] for i, j in indices]) == 4:
                risk_score += pos + 1
    
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
    
    n_rows, n_cols = len(heights), len(heights[0])
    idxi, idxj = range(n_rows), range(n_cols)
    indices = [[i, j] for i in idxi for j in idxj if heights[i][j] < 9]

    basins = []
    while len(indices):
        basin, indices = find_basin(indices)    
        basins.append(basin)
    
    basins = [len(basin) for basin in basins]
    basins.sort()
    n1, n2, n3 = basins[-3:]
    
    return n1 * n2 * n3


def run():
    
    data = load_data(filename='data/day09/test')
    solution = get_risk_score(heights=data)
    assert solution == 15

    data = load_data(filename='data/day09/input')
    solution = get_risk_score(heights=data)
    print('Part1 solution:', solution)
    assert solution == 439

    data = load_data(filename='data/day09/test')
    solution = find_basins(heights=data)
    assert solution == 1134

    data = load_data(filename='data/day09/input')
    solution = find_basins(heights=data)
    print('Part2 solution:', solution) 
    assert solution == 900900


if __name__ == '__main__':
    run()
