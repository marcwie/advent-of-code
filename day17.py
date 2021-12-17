def load_data(filename):

    with open(filename) as infile:
        
        data = infile.read()

    data = data.replace('\n', '')
    data = data.replace('target area: ', '').split(', ')
    data = [row.split('=')[1] for row in data]
    data = [row.split('..') for row in data]
    data = [int(value) for row in data for value in row]

    return data


def find_highest_position(data):
    
    _, _, ymin, _ = data
    assert ymin < 0 

    initial_velocity_y = -ymin - 1
    return initial_velocity_y * (initial_velocity_y + 1) // 2


def find_potential_velocities(data):

    xmin, xmax, ymin, _ = data

    min_v0_y = ymin
    max_v0_y = -ymin - 1

    min_v0_x = -0.5 + (2* xmin + 0.25) ** 0.5
    max_v0_x = xmax

    if not min_v0_x.is_integer():
        min_v0_x += 1
    min_v0_x = int(min_v0_x)

    vx_range = range(min_v0_x, max_v0_x + 1)
    vy_range = range(min_v0_y, max_v0_y + 1)
    return [(vx, vy) for vx in vx_range for vy in vy_range]


def simulate(data, potential_v):

    xmin, xmax, ymin, ymax = data
    n_allowed = 0 
    
    for vx, vy in potential_v:
        x, y = 0, 0
        while x < xmax and y > ymin:
            x += vx
            y += vy
            vx = (vx > 0) * (vx - 1)
            vy -= 1
            if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
                n_allowed +=1
                break

    return n_allowed


def find_initial_velocities(data):

    potential_v = find_potential_velocities(data) 
    return simulate(data, potential_v)


def run():

    data = load_data('data/day17/test')
    solution = find_highest_position(data)
    assert solution == 45

    data = load_data('data/day17/input')
    solution = find_highest_position(data)
    print('Part1 solution:', solution)
    assert solution == 3655

    data = load_data('data/day17/test')
    solution = find_initial_velocities(data)
    assert solution == 112

    data = load_data('data/day17/input')
    solution = find_initial_velocities(data)
    print('Part2 solution:', solution)
    assert solution == 1447


if __name__ == '__main__':
    run()
