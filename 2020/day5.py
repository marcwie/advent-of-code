import numpy as np

def load_data(filename):

    return np.loadtxt(filename, dtype=str)


def get_seat_id(boarding_pass):
    
    row_index = boarding_pass[:7]
    x0, x1 = 0, 128
    for i in row_index:
        if i == 'F':
            x1 = x0 + (x1 - x0) // 2
        else:
            x0 = x1 - (x1 - x0) // 2
    row = x0 

    seat_index = boarding_pass[7:]
    x0, x1 = 0, 8
    for i in seat_index:
        if i == 'L':
            x1 = x0 + (x1 - x0) // 2
        else:
            x0 = x1 - (x1 - x0) // 2
    seat = x0

    return row * 8 + seat


def part1():

    data = load_data(filename='data/day5/test')
    solution = max([get_seat_id(boarding_pass) for boarding_pass in data]) 
    assert solution == 820

    data = load_data(filename='data/day5/input')
    solution = max([get_seat_id(boarding_pass) for boarding_pass in data]) 
    print('Part1 solution:', solution)


def part2():

    data = load_data(filename='data/day5/input')
    seats = [get_seat_id(boarding_pass) for boarding_pass in data]
    seats = np.sort(seats)
    missing_seat = np.diff(seats) == 2
    missing_seat = seats[:-1][missing_seat][0] + 1
    print('Part2 solution:', missing_seat)



if __name__ == '__main__':
    part1()
    part2()
