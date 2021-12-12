import numpy as np

def run():

    data = np.loadtxt('data/day2/input', dtype=str)
    
    down = np.sum([int(value) for direction, value in data if direction == 'down'])
    forward = np.sum([int(value) for direction, value in data if direction == 'forward'])
    up = np.sum([int(value) for direction, value in data if direction == 'up'])
    print('Part1 Solution:', (down - up) * forward )
    
    depth = 0
    position = 0
    aim = 0

    for direction, value in data:
        value = int(value)
        if direction == 'forward':
            position += value
            depth += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value

    print('Part2 Solution:', position * depth )
    

if __name__ == '__main__':
    run()
