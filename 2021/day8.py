from collections import Counter


def load_data(filename='data/day8/test'):

    with open(filename) as infile:

        data = infile.read().splitlines()

    data = [row.split(' | ') for row in data] 
    data = [[row[0].split(' '), row[1].split(' ')] for row in data]

    return data


def count_number_unique_segments(data):

    output = [entry[1] for entry in data]
    flat_output = [item for entry in output for item in entry] 
    n_unique = sum([len(item) in [2, 3, 4, 7] for item in flat_output])
    
    return n_unique


def decode(inputs, outputs):
    """
        qqq
       u   v
       u   v
        www
       x   y
       x   y
        zzz
    """ 
    four_digit_combo = [entry for entry in inputs if len(entry) == 4] 
    four_digit_combo = four_digit_combo[0]

    two_digit_combo = [entry for entry in inputs if len(entry) == 2] 
    two_digit_combo = two_digit_combo[0] 

    full_string = list(''.join(inputs))
    c = Counter(full_string)
    
    mapping = {} 
    mapping['y'] = [key for key, value in c.items() if value == 9][0]
    mapping['u'] = [key for key, value in c.items() if value == 6][0]
    mapping['x'] = [key for key, value in c.items() if value == 4][0]
    mapping['q'] = [key for key, value in c.items() if value == 8 and key not in two_digit_combo][0]
    mapping['v'] = [key for key, value in c.items() if value == 8 and key != mapping['q']][0]
    mapping['w'] = [key for key, value in c.items() if value == 7 and key in four_digit_combo][0]
    mapping['z'] = [key for key, value in c.items() if value == 7 and key not in four_digit_combo][0]
    mapping = {value: key for key, value in mapping.items()}

    decoding = {'quvxyz': '0', 'vy': '1', 'qvwxz': '2', 'qvwyz': '3', 
                'uvwy': '4', 'quwyz': '5', 'quwxyz': '6', 'qvy': '7', 
                'quvwxyz': '8', 'quvwyz': '9'}
    
    decoded_output = ''
    for output in outputs:
        output = [mapping[segment] for segment in output]
        output.sort()
        output = ''.join(output)
        decoded_output += decoding[output]
    
    return int(decoded_output) 


def part1():

    data = load_data()
    n_unique = count_number_unique_segments(data=data)
    assert n_unique == 26

    data = load_data(filename='data/day8/input')
    n_unique = count_number_unique_segments(data=data)
    print('Part1 solution:', n_unique)


def part2():

    data = load_data()
    solution = sum([decode(inputs, outputs) for inputs, outputs in data])
    assert solution == 61229

    data = load_data(filename='data/day8/input')
    solution = sum([decode(inputs, outputs) for inputs, outputs in data])
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()
