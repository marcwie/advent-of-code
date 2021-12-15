def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    return data


def power_consumption(data):

    n_bits = len(data[0])
    n_numbers = len(data)
    bit_count = [0] * n_bits

    for number in data:
        for position, bit in enumerate(number):
            bit_count[position] += int(bit)

    gamma_rate = ''.join(['1' if c > (.5 * n_numbers) else '0' for c in bit_count])
    epsilon_rate = ''.join(['1' if c < (.5 * n_numbers) else '0' for c in bit_count])

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def rating(data, bit_criteria):

    other_bit = str(1 - int(bit_criteria))
    candidates = data
    position = 0

    while len(candidates) > 1:
    
        entries = [int(number[position]) for number in candidates]
        n_ones = sum(entries)
        n_zeros = len(entries) - n_ones

        if n_ones >= n_zeros:
            candidates = [n for n in candidates if n[position] == bit_criteria]
        else:
            candidates = [n for n in candidates if n[position] == other_bit]

        position += 1
    
    return int(candidates[0], 2)


def life_support_rating(data):
    return rating(data, bit_criteria='1') * rating(data, bit_criteria='0')
   

def run():

    data = load_data('data/day3/test')
    solution = power_consumption(data)
    assert solution == 198 
    
    data = load_data('data/day3/input')
    solution = power_consumption(data)
    print('Part1 solution:', solution)
    assert solution == 4118544

    data = load_data('data/day3/test')
    solution = life_support_rating(data)
    assert solution == 230
    
    data = load_data('data/day3/input')
    solution = life_support_rating(data)
    print('Part2 solution:', solution)
    assert solution == 3832770 


if __name__ == '__main__':
    run()
