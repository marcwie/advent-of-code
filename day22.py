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


def tessalate(cubes):

    pos, size, n_cube = [], [], []

    for dim in range(0, 6, 2):
        x0 = set([row[dim] for row in cubes])
        x1 = set([row[dim+1] + 1 for row in cubes])
        x0.update(x1)
        anchor = list(x0)
        anchor.sort()
        pos.append(anchor)

        dist = [anchor[i] - anchor[i-1] for i in range(1, len(anchor))]
        size.append(dist)

        n_cube.append(range(len(dist))) 
    
    idx = ((i, j, k) for i in n_cube[0] for j in n_cube[1] for k in n_cube[2])
    cubes = ([pos[0][i], pos[1][j], pos[2][k], size[0][i] * size[1][j] * size[2][k]] for i, j, k in idx)
    
    return cubes
    

def reboot(data):

    tess = tessalate(data)
    n_active = 0 
    for cube in tess:
        for x0, x1, y0, y1, z0, z1, sign in data[::-1]:
            if cube[0] < x0 or cube[0] > x1:
                continue
            if cube[1] < y0 or cube[1] > y1:
                continue
            if cube[2] < z0 or cube[2] > z1:
                continue
            if sign:
                n_active += cube[3]
            break
        
    return n_active


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


if __name__ == '__main__':
    run()
