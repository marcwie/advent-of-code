def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()
    
    coordinates = [row.split(',') for row in data if ',' in row ]
    coordinates = [[int(x), int(y)] for x, y in coordinates]

    folds = [row.rsplit(' ', 1)[-1].split('=') for row in data if '=' in row]
    folds = [(direction, int(value)) for direction, value in folds]

    return coordinates, folds


def initialize_page(coordinates):
    
    n_col = max([x for x, y in coordinates]) + 1
    n_row = max([y for x, y in coordinates]) + 1
    page = [[False for x in range(n_col)] for y in range(n_row)]
    for x, y in coordinates:
        page[y][x] = True
    
    return page


def one_fold(page, fold_along, position):

    if fold_along == 'y':
        remain = page[:position]
        fold = page[position+1:][::-1]
    else:
        remain = [row[:position] for row in page]
        fold = [row[position+1:][::-1] for row in page]
    
    idx = range(len(fold[0]))
    idy = range(len(fold))
    page = [[remain[y][x] or fold[y][x] for x in idx] for y in idy]

    return page


def fold(coordinates, folds, n_folds=None):
    
    page = initialize_page(coordinates=coordinates)

    if not n_folds:
        n_folds = len(folds)
    
    for fold_along, position in folds[:n_folds]:
        page = one_fold(page, fold_along, position)
    
    return page


def print_page(page):
    page = [''.join(['#' if l else ' ' for l in row]) for row in page]
    print('\n'.join(page))


def run():
    
    coordinates, folds = load_data(filename='data/day13/test')
    folded_page = fold(coordinates=coordinates, folds=folds, n_folds=1) 
    solution = sum([d for row in folded_page for d in row])
    assert solution == 17 

    coordinates, folds = load_data(filename='data/day13/input')
    folded_page = fold(coordinates=coordinates, folds=folds, n_folds=1) 
    solution = sum([d for row in folded_page for d in row])
    print('Part1 solution:', solution)
    assert solution == 818

    coordinates, folds = load_data(filename='data/day13/input')
    folded_page = fold(coordinates=coordinates, folds=folds) 
    print('Part2 solution:')
    print_page(folded_page)


if __name__ == '__main__':
    run()
