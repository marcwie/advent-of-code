import numpy as np

def load_data():

    with open('data/day4/input') as infile:
    
        random_numbers = infile.readline().split(',')
        random_numbers = np.array(random_numbers).astype(int)
       
        boards = np.array(infile.readlines())
        n_boards = len(boards) // 6
        
        board_list = []
        
        for i in range(n_boards):
            one_board = np.zeros((5,5))    
            for j in range(1, 6):
                row = boards[6*i+j].replace('\n', '').split(' ')
                row = [entry for entry in row if entry != '']
                row = np.array(row).astype(int)
                one_board[j-1] = row
            
            board_list.append(one_board)
    
    return random_numbers, board_list


def play_one_board(board, numbers):
    
    mask = np.zeros_like(board).astype(bool)
    
    for count, number in enumerate(numbers):
        mask = mask | (board == number)
        
        vertical = mask.all(axis=0).any()
        horizontal = mask.all(axis=1).any()
        diagonal1 = np.all([mask[i, i] for i in range(5)])
        diagonal2 = np.all([mask[i, 4-i] for i in range(5)])

        if vertical or horizontal or diagonal1 or diagonal2:
            break
    
    score = board[~mask].sum() * number

    return score, count
    

def play_all_boards(boards, numbers):

    results = np.zeros((len(boards), 2))
    for i, board in enumerate(boards):
        results[i] = play_one_board(board=board, numbers=numbers)
    
    return results


def run():

    numbers, boards = load_data()
    results = play_all_boards(boards=boards, numbers=numbers)    
       
    results_part1 = int(results[results[:, 1] == results[:, 1].min()][0, 0])
    print('Solution Part1:', results_part1)

    results_part2 = int(results[results[:, 1] == results[:, 1].max()][0, 0])
    print('Solution Part2:', results_part2)




if __name__ == '__main__':
    run()



