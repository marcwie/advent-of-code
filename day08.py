def load_data(filename='data/day08/test'):

    with open(filename) as infile:
        data = infile.read().splitlines()

    data = [row.split(' | ') for row in data] 
    return [[row[0].split(' '), row[1].split(' ')] for row in data]


def count_number_unique_segments(data):

    output = [entry[1] for entry in data]
    flat_output = [item for entry in output for item in entry] 
    return sum([len(item) in [2, 3, 4, 7] for item in flat_output])
    

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
    c = {letter: 0 for letter in set(full_string)}
    for letter in full_string:
        c[letter] += 1

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


def run():

    data = load_data()
    n_unique = count_number_unique_segments(data=data)
    assert n_unique == 26

    data = load_data(filename='data/day08/input')
    n_unique = count_number_unique_segments(data=data)
    print('Part1 solution:', n_unique)
    assert n_unique == 349

    data = load_data()
    solution = sum([decode(inputs, outputs) for inputs, outputs in data])
    assert solution == 61229

    data = load_data(filename='data/day08/input')
    solution = sum([decode(inputs, outputs) for inputs, outputs in data])
    print('Part2 solution:', solution)
    assert solution == 1070957


if __name__ == '__main__':
    run()
