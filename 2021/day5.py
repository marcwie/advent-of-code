import numpy as np

def load_data(filename='data/day5/input'):

    with open(filename) as infile:
        lines = []
        
        for line in infile.readlines():
            p0, p1 = line.replace(' ', '').replace('\n', '').split('->')
            x0, y0 = p0.split(',')
            x1, y1 = p1.split(',')
            lines.append([x0, y0, x1, y1])
        
        lines = np.array(lines).astype(int)
    
    return lines


def filter_vertical_horizontal(lines):
    lines = [[x0, y0, x1, y1] for x0, y0, x1, y1 in lines if (x0 == x1) or (y0 == y1)]
    return np.array(lines)
        

def create_ocean_map(lines):
    max_x = np.max([lines[:, 0].max(), lines[:, 2].max()])
    max_y = np.max([lines[:, 1].max(), lines[:, 3].max()])
    
    return np.zeros((max_y+1, max_x+1), dtype=int)


def fill_ocean_map(ocean_map, lines):

    for x0, y0, x1, y1 in lines:
        
        if (x0 == x1) and (y0 <= y1):
            for y in range(y0, y1+1):
                ocean_map[y, x0] += 1

        elif (x0 == x1) and (y0 > y1):
            for y in range(y0, y1-1, -1):
                ocean_map[y, x0] += 1
    
        elif (y0 == y1) and (x0 <= x1):
            for x in range(x0, x1+1):
                ocean_map[y0, x] += 1

        elif (y0 == y1) and (x0 > x1):
            for x in range(x0, x1-1, -1):
                ocean_map[y0, x] += 1
        
        elif (x0 <= x1) and (y0 <= y1):
            n_steps = y1 - y0 
            for step in range(n_steps+1):
                ocean_map[y0+step, x0+step] += 1

        elif (x0 > x1) and (y0 > y1):
            n_steps = y0 - y1 
            for step in range(n_steps+1):
                ocean_map[y0-step, x0-step] += 1

        elif (x0 <= x1) and (y0 > y1):
            n_steps = x1 - x0 
            for step in range(n_steps+1):
                ocean_map[y0-step, x0+step] += 1

        elif (x0 > x1) and (y0 <= y1):
            n_steps = y1 - y0 
            for step in range(n_steps+1):
                ocean_map[y0+step, x0-step] += 1

    return ocean_map


def print_ocean_map(ocean_map):
    
    for row in ocean_map:
        row = row.astype(str)
        row[row == '0'] = '.'
        print(''.join(row))

def part1():

    lines = load_data(filename='data/day5/input')
    lines = filter_vertical_horizontal(lines=lines)
    ocean_map = create_ocean_map(lines=lines)
    ocean_map = fill_ocean_map(ocean_map=ocean_map, lines=lines)
    n_overlaps = (ocean_map > 1).sum()

    print('Solution Part1:', n_overlaps)

    lines = load_data(filename='data/day5/input')
    ocean_map = create_ocean_map(lines=lines)
    ocean_map = fill_ocean_map(ocean_map=ocean_map, lines=lines)
    n_overlaps = (ocean_map > 1).sum()

    print('Solution Part2:', n_overlaps)



if __name__ == '__main__':
    part1()
