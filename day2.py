import numpy as np

def solve_part1(data):

    down = np.sum([int(value) for direction, value in data if direction == 'down'])
    forward = np.sum([int(value) for direction, value in data if direction == 'forward'])
    up = np.sum([int(value) for direction, value in data if direction == 'up'])
    
    return (down - up) * forward


def solve_part2(data):

    depth, position, aim = 0, 0, 0
    for direction, value in data:
        value = int(value)
        if direction == 'forward':
            position += value
            depth += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
    
    return position * depth


def run():

    data = np.loadtxt('data/day2/test', dtype=str)
    solution = solve_part1(data)
    assert solution == 150

    data = np.loadtxt('data/day2/input', dtype=str)
    solution = solve_part1(data)
    print('Part1 solution:', solution) 

    data = np.loadtxt('data/day2/test', dtype=str)
    solution = solve_part2(data)
    assert solution == 900

    data = np.loadtxt('data/day2/input', dtype=str)
    solution = solve_part2(data)
    print('Part2 solution:', solution) 


if __name__ == '__main__':
    run()
