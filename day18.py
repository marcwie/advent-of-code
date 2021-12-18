def load_data(filename):
    with open(filename) as infile:
        data = infile.read().splitlines()
    data = [row.replace(' ', '') for row in data]

    return data


def create_mapping(number):

    depth = 0
    continue_next = False
    values = []

    for i, entry in enumerate(number):
        
        if continue_next:
            continue_next = False
            continue

        if entry == '[':
            depth += 1
        elif entry == ']':
            depth -= 1
        elif entry != ',':
            if number[i+1] in [']', '[', ',']:
                value = int(entry)
            else:
                value = int(entry + number[i+1])
                continue_next = True
            values.append([value, depth])

    return values


def divide(value):
    if value % 2:
        return value // 2, value // 2 + 1
    else:
        return value // 2, value // 2


def reduce(mapping):
    
    while True:
        explode = False
        split = False

        for i in range(len(mapping)):
            value, depth = mapping[i]
            if depth == 5:
                explode = True
                break
       
        if explode:
            if i > 0:
                mapping[i-1] = [mapping[i-1][0] + value, mapping[i-1][1]]
            if i < len(mapping)-2:
                mapping[i+2] = [mapping[i+1][0] + mapping[i+2][0], mapping[i+2][1]]
            mapping[i+1] = [0, depth-1]
            mapping.pop(i)
            continue

        for i in range(len(mapping)):
            value, depth = mapping[i]
            if value >= 10:
                split = True
                break
        
        if split:
            n1, n2 = divide(value)
            mapping.pop(i)
            mapping.insert(i, [n2, depth + 1])
            mapping.insert(i, [n1, depth + 1])
            continue 
        
        break

    return mapping
            

def magnitude(number):

    while len(number) > 1:
        for i in range(len(number)-1):
            value, depth = number[i]
            if depth == number[i+1][1]:
                number[i]= [3 * value + 2 * number[i+1][0], depth-1]
                number.pop(i+1)
                break

    return number[0][0]


def add(data):

    mappings = [create_mapping(n) for n in data]
    number = mappings[0]
    
    for mapping in mappings[1:]:
        number = number + mapping
        number = [[value, depth+1] for value, depth in number]
        number = reduce(number)
    
    return magnitude(number)


def largest_magnitude(data):

    mappings = [create_mapping(n) for n in data]

    idx = range(len(mappings))
    pairs = [mappings[i] + mappings[j] for i in idx for j in idx if i != j]
    pairs = [[[value, depth+1] for value, depth in pair] for pair in pairs] 
    return max([magnitude(reduce(pair)) for pair in pairs])
    

def run():
    data = load_data(filename='data/day18/test6')
    solution = add(data)
    assert solution == 4140

    data = load_data(filename='data/day18/input')
    solution = add(data)
    print('Part1 solution:', solution)
    assert solution == 4289

    data = load_data(filename='data/day18/test6')
    solution = largest_magnitude(data)
    assert solution == 3993

    data = load_data(filename='data/day18/input')
    solution = largest_magnitude(data)
    print('Part2 solution:', solution)
    assert solution == 4807


if __name__ == '__main__':
    run()
