import numpy as np


def load_data(filename):

    with open(filename) as infile:
        
        data = infile.read().splitlines()
    
    coordinates = [row.split(',') for row in data if ',' in row ]
    coordinates = np.array(coordinates).astype(int)
    
    folds = [row.rsplit(' ', 1)[-1].split('=') for row in data if '=' in row]
    folds = [(direction, int(value)) for direction, value in folds]

    return coordinates, folds


def initialize_page(coordinates):
    
    n_cols, n_rows = coordinates.max(axis=0) + 1
    page = np.zeros((n_rows, n_cols), dtype=bool)
    page[coordinates[:, 1], coordinates[:, 0]] = True
    
    return page


def one_fold(page, fold_along, position):

    if fold_along == 'y':
        return page[:position] + np.flipud(page[position+1:])
    else:
        return page[:, :position] + np.fliplr(page[:, position+1:])


def fold(coordinates, folds, n_folds=None):
    
    page = initialize_page(coordinates=coordinates)
    
    if not n_folds:
        n_folds = len(folds)
    
    for fold_along, position in folds[:n_folds]:
        page = one_fold(page, fold_along, position)
    
    return page


def print_page(page):
    
    page_str = ''
    page = page.astype(str)
    page[page == 'True'] = '#'
    page[page == 'False'] = ' '

    for row in page:
        page_str += ''.join(row) + '\n'
    print(page_str)


def run():
    
    coordinates, folds = load_data(filename='data/day13/test')
    folded_page  = fold(coordinates=coordinates, folds=folds, n_folds=1) 
    solution = folded_page.sum()
    assert solution == 17 

    coordinates, folds = load_data(filename='data/day13/input')
    folded_page = fold(coordinates=coordinates, folds=folds, n_folds=1) 
    solution = folded_page.sum()
    print('Part1 solution:', solution)
    assert solution == 818

    coordinates, folds = load_data(filename='data/day13/input')
    folded_page = fold(coordinates=coordinates, folds=folds) 
    print('Part2 solution:')
    print_page(folded_page)


if __name__ == '__main__':
    run()
