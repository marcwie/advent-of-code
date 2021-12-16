def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    
    data = [[bin(int(d, 16))[2:].zfill(4) for d in row] for row in data]
    data = [''.join(row) for row in data]
    if len(data) == 1:
        data = data[0]

    return data


def get_version(data, pos):
    version = int(data[pos:pos+3], 2)
    return version, pos+3


def get_type_id(data, pos):
    type_id = int(data[pos:pos+3], 2)
    return type_id, pos+3


def get_length_type_id(data, pos):
    return int(data[pos]), pos+1


def get_subpackage_length(data, pos):
    length = int(data[pos:pos+15], 2)
    return pos+15+length, pos+15


def get_number_subpackages(data, pos):
    n_packages = int(data[pos:pos+11], 2)
    return n_packages, pos+11


def prod(values):
    result = 1
    for val in values:
        result *= val
    return result


def gg(x0, x1):
    return int(x0 > x1)


def ll(x0, x1):
    return int(x0 < x1)


def eq(x0, x1):
    return int(x0 == x1)


def parse_literal(data, pos):
    end = list(data[pos::5]).index('0')
    number = ''.join([data[pos+1+i*5:pos+5+i*5] for i in range(end+1)])
    return int(number, 2), pos+5+end*5


def parse_operator(data, pos, type_id, version_sum):
    
    operation = {0: sum, 1: prod, 2: min, 3: max, 5: gg, 6: ll, 7: eq}
    length_type_id, pos = get_length_type_id(data, pos)

    values = []
    if not length_type_id:
        length, pos = get_subpackage_length(data, pos)
        while pos < length:
            value, version_sum, pos = parse_package(data, version_sum, pos)
            values.append(value)
    else:
        n_packages, pos = get_number_subpackages(data, pos)
        for _ in range(n_packages):
            value, version_sum, pos = parse_package(data, version_sum, pos)
            values.append(value)
    
    if type_id > 4:
        return operation[type_id](values[0], values[1]), version_sum, pos
    else:
        return operation[type_id](values), version_sum, pos


def parse_package(data, version_sum=0, pos=0):

    version, pos = get_version(data, pos) 
    type_id, pos = get_type_id(data, pos) 
    version_sum += version 

    if type_id == 4:
        value, pos = parse_literal(data, pos)
    else:
        value, version_sum, pos = parse_operator(data, pos, type_id, version_sum)
    
    return value, version_sum, pos


def run():

    data = load_data(filename='data/day16/test')
    solutions = [16, 12, 23, 31]
    for i, d in enumerate(data):
        _, version_sum, _ = parse_package(d)
        assert version_sum == solutions[i]

    data = load_data(filename='data/day16/input')
    _, version_sum, _ = parse_package(data)
    print('Part1 solution:', version_sum)
    assert version_sum == 843

    data = load_data(filename='data/day16/test2')
    solutions = [3, 54, 7, 9, 1, 0, 0, 1]
    for i, d in enumerate(data):
        value, _, _ = parse_package(d)
        assert value == solutions[i]

    data = load_data(filename='data/day16/input')
    value, _, _ = parse_package(data)
    print('Part2 solution:', value)
    assert value == 5390807940351
    

if __name__ == '__main__':
    run()
