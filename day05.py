def load_data(filename='data/day05/input'):

    with open(filename) as infile:

        lines = []
        for line in infile.readlines():
            p0, p1 = line.replace(' ', '').replace('\n', '').split('->')
            x0, y0 = p0.split(',')
            x1, y1 = p1.split(',')
            lines.append([int(x0), int(y0), int(x1), int(y1)])
        
    return lines


def filter_vertical_horizontal(lines):
    return [[x0, y0, x1, y1] for x0, y0, x1, y1 in lines if (x0 == x1) or (y0 == y1)]
        

def create_ocean_map(lines):
    max_x = max([max([l[0] for l in lines]), max([l[2] for l in lines])])
    max_y = max([max([l[1] for l in lines]), max([l[3] for l in lines])])
    return [[0] * (max_x + 1) for _ in range(max_y+1)]


def fill_ocean_map(ocean_map, lines):

    for x0, y0, x1, y1 in lines:
        
        if (x0 == x1) and (y0 <= y1):
            for y in range(y0, y1+1):
                ocean_map[y][x0] += 1

        elif (x0 == x1) and (y0 > y1):
            for y in range(y0, y1-1, -1):
                ocean_map[y][x0] += 1
    
        elif (y0 == y1) and (x0 <= x1):
            for x in range(x0, x1+1):
                ocean_map[y0][x] += 1

        elif (y0 == y1) and (x0 > x1):
            for x in range(x0, x1-1, -1):
                ocean_map[y0][x] += 1
        
        elif (x0 <= x1) and (y0 <= y1):
            n_steps = y1 - y0 
            for step in range(n_steps+1):
                ocean_map[y0+step][x0+step] += 1

        elif (x0 > x1) and (y0 > y1):
            n_steps = y0 - y1 
            for step in range(n_steps+1):
                ocean_map[y0-step][x0-step] += 1

        elif (x0 <= x1) and (y0 > y1):
            n_steps = x1 - x0 
            for step in range(n_steps+1):
                ocean_map[y0-step][x0+step] += 1

        elif (x0 > x1) and (y0 <= y1):
            n_steps = y1 - y0 
            for step in range(n_steps+1):
                ocean_map[y0+step][x0-step] += 1

    return ocean_map


def print_ocean_map(ocean_map):
    
    for row in ocean_map:
        row = row.astype(str)
        row[row == '0'] = '.'
        print(''.join(row))


def solve_part1(lines):

    lines = filter_vertical_horizontal(lines=lines)
    ocean_map = create_ocean_map(lines=lines)
    ocean_map = fill_ocean_map(ocean_map=ocean_map, lines=lines)
    n_overlaps = sum([n > 1 for row in ocean_map for n in row])

    return n_overlaps


def solve_part2(lines):

    ocean_map = create_ocean_map(lines=lines)
    ocean_map = fill_ocean_map(ocean_map=ocean_map, lines=lines)
    n_overlaps = sum([n > 1 for row in ocean_map for n in row])
    
    return n_overlaps


def run():

    lines = load_data(filename='data/day05/test')
    solution = solve_part1(lines)
    assert solution == 5

    lines = load_data(filename='data/day05/input')
    solution = solve_part1(lines)
    print('Solution Part1:', solution)
    assert solution == 7142

    lines = load_data(filename='data/day05/test')
    solution = solve_part2(lines)
    assert solution == 12

    lines = load_data(filename='data/day05/input')
    solution = solve_part2(lines)
    print('Solution Part2:', solution)
    assert solution == 20012


if __name__ == '__main__':
    run()
