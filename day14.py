def load_data(filename):

    with open(filename, 'r') as infile:

        lines = infile.read().splitlines()

    template = lines[0]
    mapping = dict([line.split(' -> ') for line in lines[2:]])

    return template, mapping


def count_letters(counter, first_letter, last_letter):

    unique_letter = {letter for pair in counter.keys() for letter in pair}
    letter_count = {letter: 0 for letter in unique_letter}

    for pair, count in counter.items():
        letter_count[pair[0]] += count
        letter_count[pair[1]] += count

    letter_count[first_letter] += 1
    letter_count[last_letter] += 1

    letter_count = [count // 2 for count in letter_count.values()]
    
    return letter_count
    

def one_step(counter, mapping):

    new_pairs = [[p[0] + mapping[p], mapping[p] + p[1], c] for p, c in counter.items()]
        
    counter = {key: 0 for key in mapping.keys()}
    for p1, p2, count in new_pairs:
        counter[p1] += count
        counter[p2] += count
    
    return counter


def insert(template, mapping, n_reps):
    
    # Count pairs in original template
    counter = {key: 0 for key in mapping.keys()}
    pairs = [template[i:i+2] for i in range(len(template) - 1)]
    for pair in pairs:
        counter[pair] += 1
    
    # Update the pair counter iteratively
    for _ in range(n_reps):
        counter = one_step(counter, mapping) 
  
    # Count letters in final polymer
    letter_count = count_letters(counter, template[0], template[-1])
    
    return max(letter_count) - min(letter_count)


def run():

    template, mapping = load_data('data/day14/test')
    solution = insert(template=template, mapping=mapping, n_reps=10)
    assert solution == 1588

    template, mapping = load_data('data/day14/input')
    solution = insert(template=template, mapping=mapping, n_reps=10)
    print('Part1 solution:', solution)
    assert solution == 4517

    template, mapping = load_data('data/day14/test')
    solution = insert(template=template, mapping=mapping, n_reps=40)
    assert solution == 2188189693529

    template, mapping = load_data('data/day14/input')
    solution = insert(template=template, mapping=mapping, n_reps=40)
    print('Part2 solution:', solution)
    assert solution == 4704817645083


if __name__ == '__main__':
    run()
