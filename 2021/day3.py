import numpy as np


def part1():
    
    data = np.loadtxt('data/day3/input', dtype=str)
    
    n_bits = len(data[0])
    n_numbers = len(data)
    bit_count = np.zeros(n_bits)

    for number in data:
        for position, bit in enumerate(number):
            bit_count[position] += int(bit)

    gamma_rate = ''.join((bit_count > (.5 * n_numbers)).astype(int).astype(str))
    epsilon_rate = ''.join((bit_count < (.5 * n_numbers)).astype(int).astype(str))

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print('Part1 Solution:', gamma_rate * epsilon_rate )


def part2():
    
    data = np.loadtxt('data/day3/input', dtype=str)

    candidates = data
    position = 0
    
    while len(candidates) > 1:
    
        entries = np.array([int(number[position]) for number in candidates])
        n_ones = entries.sum()
        n_zeros = len(entries) - n_ones

        if n_ones >= n_zeros:
            candidates = [number for number in candidates if number[position] == '1']
        else:
            candidates = [number for number in candidates if number[position] == '0']

        position += 1
        
    oxygen_rating = int(candidates[0], 2)

    candidates = data
    position = 0
    
    while len(candidates) > 1:
    
        entries = np.array([int(number[position]) for number in candidates])
        n_ones = entries.sum()
        n_zeros = len(entries) - n_ones

        if n_ones >= n_zeros:
            candidates = [number for number in candidates if number[position] == '0']
        else:
            candidates = [number for number in candidates if number[position] == '1']

        position += 1
        
    co2_scrubber_rating = int(candidates[0], 2)

    print('Part2 Solution:', co2_scrubber_rating * oxygen_rating)
   

if __name__ == '__main__':
    part1()
    part2()
