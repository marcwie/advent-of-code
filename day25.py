def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()

    data = [list(row) for row in data]
    row, col = len(data), len(data[0])
    idi, idj = range(row), range(col)

    east_facing = [(i, j) for i in idi for j in idj if data[i][j] == '>']
    south_facing = [(i, j) for i in idi for j in idj if data[i][j] == 'v']
    none = [(i, j) for i in idi for j in idj if data[i][j] == '.']
    
    return east_facing, south_facing, row, col


def move(east, south, row, col):
    
    is_moving, counter = True, 0

    while is_moving:

        is_moving, counter = False, counter + 1
        new_east, new_south  = [], []
        
        n_move = 0
        for i, j in east:
            if (i, (j+1) % col) not in east and (i, (j+1) % col) not in south:
                new_east.append((i, (j+1) % col))
                is_moving = True
                n_move += 1
            else:
                new_east.append((i, j))
        east = new_east

        for i, j in south:
            if ((i+1) % row, j) not in east and ((i+1) % row, j) not in south:
                new_south.append(((i+1) % row, j))
                is_moving = True
                n_move += 1
            else:
                new_south.append((i, j))
        south = new_south

    return counter


def run():

    east, south, row, col = load_data(filename='data/day25/test')
    solution = move(east, south, row, col)
    assert solution == 58

    print('Computing solution. Takes a while...')
    east, south, row, col = load_data(filename='data/day25/input')
    solution = move(east, south, row, col)
    print('Solution:', solution)
    assert solution == 458


if __name__ == '__main__':
    run()
