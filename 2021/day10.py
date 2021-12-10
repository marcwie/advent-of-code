def load_data(filename='data/day10/test'):

    with open(filename) as infile:

        data = infile.read().splitlines()

    return data


def validate(line):
   
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    expected_closing = []
     
    for character in line:
        if character in matches.keys():
            expected_closing.append(matches[character])
        if character in matches.values():
            expected = expected_closing.pop()
            if expected != character:
                return points[character]

    return 0


def autocomplete(line):
   
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 1, ']': 2, '}': 3, '>': 4}

    expected_closing = []
     
    for character in line:
        if character in matches.keys():
            expected_closing.append(matches[character])
        if character in matches.values():
            expected = expected_closing.pop()
            if expected != character:
                return 0
        
    total_score = 0
    while len(expected_closing):
        total_score *= 5
        expected = expected_closing.pop()
        total_score += points[expected]

    return total_score


def find_middle_score(scores):

    scores = [score for score in scores if score > 0]
    n_scores = len(scores)
    scores.sort()
    return scores[(n_scores - 1) // 2]


def part1():

    data = load_data(filename='data/day10/test')
    solution = sum([validate(line) for line in data])
    assert solution == 26397

    data = load_data(filename='data/day10/input')
    solution = sum([validate(line) for line in data])
    print('Part1 solution:', solution)


def part2():

    data = load_data(filename='data/day10/test')
    solution = [autocomplete(line) for line in data]
    solution = find_middle_score(solution)
    assert solution == 288957

    data = load_data(filename='data/day10/input')
    solution = [autocomplete(line) for line in data]
    solution = find_middle_score(solution)
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()
