from collections import Counter
import numpy as np


def load_data(filename):
    
    with open(filename) as infile:
        
        data = infile.read().splitlines()
    
    links = [row.split('-') for row in data]
    nodes = list(set([x for row  in links for x in row]))
    
    network = {node: [] for node in nodes}
    
    for v1, v2 in links:
        network[v1].append(v2)
        network[v2].append(v1)

    return network


def run(network):

    paths = [['start',],]
    is_running = True
    
    while is_running:
        is_running = False

        # An empty list for the next iteration
        next_step = []

        # Iterate over every currently existing path
        for path in paths:
            current_node = path[-1]

            # If the path is already at the end node store it
            if current_node == 'end':
                next_step.append(path)

            # Otherwise we go to all next valid nodes and store that section of
            # the path
            else:
                for next_node in network[current_node]:
                    if next_node.lower() not in path:
                        next_step.append(path + [next_node])
                        is_running = True

        paths = next_step        

    return paths


def is_valid_path(path):

    if 'start' in path[1:]:
        return False

    if 'end' in path[:-1]:
        return False

    small_caves = [node for node in path if node == node.lower()] 
    n_caves = np.array([v for v in Counter(small_caves).values()])
    if (n_caves > 2).any() or ((n_caves == 2).sum() > 1):
        return False

    return True
    

def run_part2(network):

    paths = [['start',],]
    is_running = True

    while is_running:
        is_running = False

        # An empty list for the next iteration
        next_step = []

        # Iterate over every currently existing path
        for path in paths:
            current_node = path[-1]
        
            if current_node == 'end':
                next_step.append(path)

            else:
               for next_node in network[current_node]:
                    new_path = path + [next_node]
                    if is_valid_path(new_path):
                        next_step.append(new_path)
                        is_running = True
        
        paths = next_step        

    return paths


def part1():

    network = load_data(filename='data/day12/test')
    solution = len(run(network=network))
    assert solution == 10

    network = load_data(filename='data/day12/test2')
    solution = len(run(network=network))
    assert solution == 19

    network = load_data(filename='data/day12/test3')
    solution = len(run(network=network))
    assert solution == 226

    network = load_data(filename='data/day12/input')
    solution = len(run(network=network))
    print('Part1 solution:', solution)


def part2():

    network = load_data(filename='data/day12/test')
    solution = len(run_part2(network=network))
    assert solution == 36

    network = load_data(filename='data/day12/test2')
    solution = len(run_part2(network=network))
    assert solution == 103

    network = load_data(filename='data/day12/test3')
    solution = len(run_part2(network=network))
    assert solution == 3509
        
    network = load_data(filename='data/day12/input')
    solution = len(run_part2(network=network))
    print('Part2 solution:', solution)

 
if __name__ == '__main__':
    part1()
    part2()

