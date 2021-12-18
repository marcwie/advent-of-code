def load_data(filename='data/day07/test'):

    with open(filename) as infile:
        data = infile.readline().split(',')
    data = [int(n) for n in data]
    data.sort()

    return data


def weighted_consumption(data):
    
    min_x = min(data)
    max_x = max(data)
    
    consumptions = []
    for final_x in range(min_x, max_x+1):
        distance = [abs(d - final_x) for d in data]
        consumptions.append(sum([d * (d + 1) // 2 for d in distance]))
    
    return min(consumptions)


def median(data):
    n_data = len(data)
    if not (n_data % 2):
        return sum(data[n_data//2-1:n_data//2+1]) // 2
    else:
        return data[n_data//2]

def consumption(data):
    return sum([abs(d - median(data)) for d  in data])


def run():
    
    data = load_data('data/day07/test')
    solution = consumption(data) 
    assert solution == 37

    solution = weighted_consumption(data)
    assert solution == 168

    data = load_data('data/day07/input')
    solution = consumption(data) 
    print('Part1 solution:', solution)
    assert solution == 354129

    solution = weighted_consumption(data)
    print('Part2 solution:', solution)
    assert solution == 98905973


if __name__ == '__main__':
    run()
