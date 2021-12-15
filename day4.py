def load_data(filename):

    with open(filename) as infile:
    
        random_numbers = infile.readline().split(',')
        boards = infile.readlines()

    random_numbers = [int(n) for n in random_numbers]
       
    n_boards = len(boards) // 6
    board_list = []

    for i in range(n_boards):
        one_board = []     

        for j in range(1, 6):
            row = boards[6*i+j].replace('\n', '').split(' ')
            row = [entry for entry in row if entry != '']
            row = [int(n) for n in row]
            one_board.append(row)
        
        board_list.append(one_board)
    
    return random_numbers, board_list


def play_one_board(board, numbers):
    
    flat_board = [n for row in board for n in row]
    mask = [False] * len(flat_board)
    
    score = sum(flat_board)
    for count, number in enumerate(numbers):

        if number in flat_board:
            mask[flat_board.index(number)] = True
            score -= number
        
        for i in range(len(board)):
            if False not in mask[i::5] or False not in mask[5*i:5*(i+1)]:
                return score * number, count
    

def play_all_boards(boards, numbers, find='first'):

    results = []
    for i, board in enumerate(boards):
        results.append(play_one_board(board=board, numbers=numbers))
    
    rounds = [rounds for _, rounds in results]
    if find == 'first':
        index = rounds.index(min(rounds))
    else:
        index = rounds.index(max(rounds))

    return results[index][0]


def run():

    numbers, boards = load_data(filename='data/day4/test')
    solution = play_all_boards(boards=boards, numbers=numbers, find='first')    
    assert solution == 4512

    solution = play_all_boards(boards=boards, numbers=numbers, find='last')    
    assert solution == 1924

    numbers, boards = load_data(filename='data/day4/input')
    solution = play_all_boards(boards=boards, numbers=numbers, find='first')    
    print('Solution Part1:', solution)
    assert solution == 51034

    solution = play_all_boards(boards=boards, numbers=numbers, find='last')    
    print('Solution Part2:', solution)
    assert solution == 5434


if __name__ == '__main__':
    run()
