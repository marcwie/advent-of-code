def load_data(filename):
    
    with open(filename) as infile:
        
        data = infile.read().splitlines()
    
    links = [row.split('-') for row in data]
    nodes = list(set([x for row  in links for x in row]))
    
    network = {node: [] for node in nodes}
    
    for v1, v2 in links:
        if v1 != 'end' and v2 != 'start':
            network[v1].append(v2)
        if v2 != 'end' and v1 != 'start':
            network[v2].append(v1)

    return network


def is_valid_path(path, small_caves, n_double_visits=1):
    
    double_visits = 0
    for cave in small_caves:
        n_visits = path.count(cave)

        if n_visits > 2:
            return False

        if (n_visits == 2):
            double_visits += 1

        if double_visits > n_double_visits:
            return False

    return True
    

def run(network, n_double_visits=1):

    paths = [['start',],]
    is_running = True
    small_caves = [key for key in network.keys() if key == key.lower()]

    while is_running:
        is_running = False

        # An empty list for the next iteration
        next_step = []

        # Iterate over every currently existing path
        for path in paths:
            current_node = path[-1]
        
            if current_node == 'end':
                next_step.append(path)
                continue 

            for next_node in network[current_node]:
                new_path = path + [next_node]
                if is_valid_path(new_path, small_caves, n_double_visits):
                    next_step.append(new_path)
                    is_running = True
        
        paths = next_step        

    return paths


def part1():

    network = load_data(filename='data/day12/test')
    solution = len(run(network=network, n_double_visits=0))
    assert solution == 10

    network = load_data(filename='data/day12/test2')
    solution = len(run(network=network, n_double_visits=0))
    assert solution == 19

    network = load_data(filename='data/day12/test3')
    solution = len(run(network=network, n_double_visits=0))
    assert solution == 226

    network = load_data(filename='data/day12/input')
    solution = len(run(network=network, n_double_visits=0))
    print('Part1 solution:', solution)


def part2():

    network = load_data(filename='data/day12/test')
    solution = len(run(network=network))
    assert solution == 36

    network = load_data(filename='data/day12/test2')
    solution = len(run(network=network))
    assert solution == 103

    network = load_data(filename='data/day12/test3')
    solution = len(run(network=network))
    assert solution == 3509
        
    network = load_data(filename='data/day12/input')
    solution = len(run(network=network))
    print('Part2 solution:', solution)

 
if __name__ == '__main__':
    part1()
    part2()

