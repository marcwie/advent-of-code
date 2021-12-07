import numpy as np
from itertools import combinations


def load_data(filename='data/day1/test'):
    
    return np.loadtxt(filename, dtype=int)


def find_numbers_that_add_to_2020(numbers, n_numbers=2):
    
    for candidates in combinations(numbers, n_numbers):
        if sum(candidates) == 2020:
            return candidates

    
def part1():
    
    numbers = load_data('data/day1/test')
    n1, n2 = find_numbers_that_add_to_2020(numbers=numbers)
    solution = n1 * n2
    assert solution == 514579

    numbers = load_data('data/day1/input')
    n1, n2 = find_numbers_that_add_to_2020(numbers=numbers)
    solution = n1 * n2
    print('Part1 solution:', solution) 


def part2():
    
    numbers = load_data('data/day1/test')
    n1, n2, n3 = find_numbers_that_add_to_2020(numbers=numbers, n_numbers=3)
    solution = n1 * n2 * n3
    assert solution == 241861950

    numbers = load_data('data/day1/input')
    n1, n2, n3 = find_numbers_that_add_to_2020(numbers=numbers, n_numbers=3)
    solution = n1 * n2 * n3
    print('Part2 solution:', solution) 


if __name__ == '__main__':
    part1()
    part2()
