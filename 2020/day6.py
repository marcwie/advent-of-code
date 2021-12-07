def load_data(filename):

    with open(filename) as infile:
        lines = infile.read()

    lines = lines[:-1]
    lines = lines.split('\n\n')
    lines = [line.split('\n') for line in lines]

    return lines


def count_unique_answers(group):

    return len(set(''.join(group)))


def count_joint_answers(group):
    
    group = [set(entry) for entry in group]
    return len(set.intersection(*group))


def part1():

    data = load_data(filename='data/day6/test')
    n_answers = [count_unique_answers(group) for group in data]
    solution = sum(n_answers)
    assert solution == 11

    data = load_data(filename='data/day6/input')
    n_answers = [count_unique_answers(group) for group in data]
    solution = sum(n_answers)
    print('Part1 solution:', solution)


def part2():

    data = load_data(filename='data/day6/test')
    n_answers = [count_joint_answers(group) for group in data]
    solution = sum(n_answers)
    assert solution == 6

    data = load_data(filename='data/day6/input')
    n_answers = [count_joint_answers(group) for group in data]
    solution = sum(n_answers)
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()
