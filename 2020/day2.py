def load_data(filename):
    
    data = []
    with open(filename) as infile:
        for line in infile.readlines():
            policy, password = line.split(':')
            allowed_range, letter = policy.split(' ')
            min_range, max_range = allowed_range.split('-')
            password = password.replace(' ', '')
            data.append([int(min_range), int(max_range), letter, password])

    return data


def is_valid(min_range, max_range, letter, password):
    
    n_occurences = len([l for l in password if l == letter])
    return (n_occurences >= min_range) and (n_occurences <= max_range)

   
def letter_at_one_position(pos1, pos2, letter, password):
    
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)


def part1():
    
    data = load_data(filename='data/day2/test')
    solution = sum([is_valid(x0, x1, x2, x3) for x0, x1, x2, x3 in data])
    assert solution == 2

    data = load_data(filename='data/day2/input')
    solution = sum([is_valid(x0, x1, x2, x3) for x0, x1, x2, x3 in data])
    print('Part1 solution:', solution)


def part2():
    
    data = load_data(filename='data/day2/test')
    solution = sum([letter_at_one_position(x0, x1, x2, x3) for x0, x1, x2, x3 in data])
    assert solution == 1

    data = load_data(filename='data/day2/input')
    solution = sum([letter_at_one_position(x0, x1, x2, x3) for x0, x1, x2, x3 in data])
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()


