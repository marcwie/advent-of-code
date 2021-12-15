def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    data = [row.split(' ') for row in data]

    return [[direction, int(value)] for direction, value in data]


def solve_part1(data):

    down = sum([val for direction, val in data if direction == 'down'])
    forward = sum([val for direction, val in data if direction == 'forward'])
    up = sum([val for direction, val in data if direction == 'up'])
    
    return (down - up) * forward


def solve_part2(data):

    depth, position, aim = 0, 0, 0
    for direction, value in data:
        if direction == 'forward':
            position += value
            depth += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
    
    return position * depth


def run():

    data = load_data('data/day2/test')
    solution = solve_part1(data)
    assert solution == 150

    data = load_data('data/day2/input')
    solution = solve_part1(data)
    print('Part1 solution:', solution) 
    assert solution == 2120749

    data = load_data('data/day2/test')
    solution = solve_part2(data)
    assert solution == 900

    data = load_data('data/day2/input')
    solution = solve_part2(data)
    print('Part2 solution:', solution) 
    assert solution == 2138382217


if __name__ == '__main__':
    run()
