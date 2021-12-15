def load_data(filename, expand=False):

    with open(filename) as infile:
        data = infile.read().splitlines()
    
    if expand:
        data = expand_data(data)

    node_weights = [int(entry) for row in data for entry in row]
    
    neighbors = []
    for i, row in enumerate(data):
        for j, entry in enumerate(row):
            nbs = [[i-1, j], [i+1, j], [i, j+1], [i, j-1]]
            nbs = [i * len(row) + j for i, j in nbs if i >= 0 and i < len(data) and j >=0 and j < len(row)]
            neighbors.append(nbs)        

    return node_weights, neighbors


def expand_data(data):
    
    expanded_data = []
    n_rows = len(data)

    for row in data:
        row = [int(entry) for entry in row] 
        new_row = row
        for i in range(1, 5):
            append = [entry + i if (entry + i) < 10 else (entry + i - 9) for entry in row]
            new_row = new_row + append
        expanded_data.append(new_row)
    
    for i in range(1, 5):
        for row_index in range(n_rows):
            row = expanded_data[row_index]
            new_row = [entry + i if (entry + i) < 10 else (entry + i - 9) for entry in row]
            expanded_data.append(new_row)

    expanded_data = [''.join([str(entry) for entry in row]) for row in expanded_data]
    
    return expanded_data


def find_lowest_risk(node_weights, neighbors):
    
    n_nodes = len(node_weights)
    max_risk = sum(node_weights)

    risk = [max_risk] * n_nodes

    risk[0] = 0 
    dummy_risk = [0]

    visited = set()
    unvisited = set(range(n_nodes)) 
    
    while unvisited:

        min_risk = min(dummy_risk) 
        dummy_risk.remove(min_risk)
        for active in unvisited:
            if risk[active] == min_risk:
                break
        
        visited.add(active)
        unvisited.remove(active)

        for neighbor in neighbors[active]:
            if risk[neighbor] > risk[active] + node_weights[neighbor]:
                risk[neighbor] = risk[active] + node_weights[neighbor]
                dummy_risk.append(risk[neighbor])
    
    return risk[-1]
    

def run():
    
    node_weights, neighbors = load_data(filename='data/day15/test')
    solution = find_lowest_risk(node_weights, neighbors)
    assert solution == 40

    node_weights, neighbors = load_data(filename='data/day15/input')
    solution = find_lowest_risk(node_weights, neighbors)
    print('Part1 solution:', solution)
    assert solution == 626

    node_weights, neighbors = load_data(filename='data/day15/test', expand=True)
    solution = find_lowest_risk(node_weights, neighbors)
    assert solution == 315

    print('Running part 2. Takes a while...')
    node_weights, neighbors = load_data(filename='data/day15/input', expand=True)
    solution = find_lowest_risk(node_weights, neighbors)
    print('Part2 solution:', solution)
    assert solution == 2966


if __name__ == '__main__':
    run()
