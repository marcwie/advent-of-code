import numpy as np


def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
        data = [list(row) for row in data]
    
    return np.array(data)


def count_trees(geology, down, right):
    x, y = 0, 0
    n_y, n_x = geology.shape
    n_trees = 0 
    
    while y < n_y:
        n_trees += geology[y, x] == '#'
        y += down
        x += right
        if x >= n_x:
            x -= n_x

    return n_trees


def find_product(geology):

    directions = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    product = 1 

    for down, right in directions:
        product *= count_trees(geology=geology, down=down, right=right)

    return product


def part1():

    geology = load_data('data/day3/test')
    solution = count_trees(geology=geology, down=1, right=3)    
    assert solution == 7

    geology = load_data('data/day3/input')
    solution = count_trees(geology=geology, down=1, right=3)    
    print('Part1 solution:', solution)


def part2():

    geology = load_data('data/day3/test')
    solution = find_product(geology=geology)    
    assert solution == 336

    geology = load_data('data/day3/input')
    solution = find_product(geology=geology)    
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()


