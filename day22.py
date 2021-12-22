def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    
    data = [row.split(' ') for row in data]

    signal = [1 if row[0] == 'on' else 0 for row in data]
    data = [row[1].split(',') for row in data]
    data = [[e[2:].split('..') for e in row] for row in data]
    data = [[int(e) for pair in row for e in pair] for row in data]
    data = [data[i] + [signal[i]] for i in range(len(data))]

    return data


def find_intersections(data):
    
    isects, size = [], []

    for dim in range(0, 6, 2):
        x0 = set([row[dim] for row in data])
        x1 = set([row[dim+1] + 1 for row in data])
        x0.update(x1)
        anchor = list(x0)
        anchor.sort()

        dist = [anchor[i] - anchor[i-1] for i in range(1, len(anchor))]
        size.append(dist)
        isects.append(anchor[:-1])

    return isects, size
 

def reboot(data):
    
    isects, size = find_intersections(data)
    states = {}    

    for i, (x0, x1, y0, y1, z0, z1, sign) in enumerate(data):
        xsects = [i for i, x in enumerate(isects[0]) if x >= x0 and x <= x1]
        ysects = [i for i, y in enumerate(isects[1]) if y >= y0 and y <= y1]
        zsects = [i for i, z in enumerate(isects[2]) if z >= z0 and z <= z1]
        subcubes = ((i, j, k) for i in xsects for j in ysects for k in zsects)
        for i, j, k in subcubes:
            states[(i, j, k)] = sign * size[0][i] * size[1][j] * size[2][k]

    return sum(states.values())


def crop(data, vmin, vmax):

    for i in range(len(data)):
        for dim in range(0, 6, 2):
            data[i][dim] = max([data[i][dim], vmin])
            data[i][dim+1] = min([data[i][dim+1], vmax])
    return [r for r in data if r[1] >= r[0] and r[3] >= r[2] and r[5] >= r[4]]


def run():
    data = load_data('data/day22/test')
    data = crop(data, -50, 50)
    solution = reboot(data)
    assert solution == 39

    data = load_data('data/day22/test2')
    data = crop(data, -50, 50)
    solution = reboot(data)
    assert solution == 590784

    data = load_data('data/day22/test3')
    data = crop(data, -50, 50)
    solution = reboot(data)
    assert solution == 474140

    data = load_data('data/day22/input')
    data = crop(data, -50, 50)
    solution = reboot(data)
    print('Part1 solution:', solution)
    assert solution == 533863

    data = load_data('data/day22/test3')
    solution = reboot(data)
    assert solution == 2758514936282235
    
    data = load_data('data/day22/input')
    print('Computing part 2. Takes a while...')
    solution = reboot(data)
    print('Part2 solution:', solution)
    assert solution == 1261885414840992


if __name__ == '__main__':
    run()
