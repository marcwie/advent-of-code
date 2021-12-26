COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def part1():
    burrow = {i: None for i in range(11)}
    rooms = {
        20: 'D1', 21: 'D2', 
        40: 'A1', 41: 'C1', 
        60: 'C2', 61: 'B1', 
        80: 'A2', 81: 'B2'
    }

    burrow.update(rooms)
    final_hallway = {
        'A': [20, 21], 
        'B': [40, 41], 
        'C': [60, 61], 
        'D': [80, 81]
    }

    return burrow, final_hallway


def part2():
    burrow = {i: None for i in range(11)}
    rooms = {
        20: 'D1', 21: 'D2', 22: 'D3', 23: 'D4', 
        40: 'A1', 41: 'C1', 42: 'B1', 43: 'C2',
        60: 'C3', 61: 'B2', 62: 'A2', 63: 'B3',
        80: 'A3', 81: 'A4', 82: 'C4', 83: 'B4'
    }
    
    burrow.update(rooms)
    final_hallway = {
        'A': [20, 21, 22, 23], 
        'B': [40, 41, 42, 43], 
        'C': [60, 61, 62, 63], 
        'D': [80, 81, 82, 83]
    }

    return burrow, final_hallway


def find_players_that_move(state, final_hallway):

    player_positions = {value: key for key, value in state.items() if value}
    
    active_players = []
    for player, position in player_positions.items():
        kind, number = list(player)
        goal = final_hallway[kind]    

        # If player has already reached goal, don't move
        if position in goal:
            if all([kind in state[pos] for pos in goal if pos >= position]):
                continue

        # If player is in hallway, but the rooms are blocked, don't move
        if position <= 10:
            if not all([state[pos][0] == str(kind) for pos in goal if state[pos]]):
                continue

        # If player is blocked in room, don't move
        if position > 10:
            if (position - 1) in state.keys() and state[position-1] != None:
                continue
        active_players.append(player) 

        
    return active_players


def find_moves(state, cost, player, final_hallway):
    
    player_positions = {value: key for key, value in state.items() if value}
    position = player_positions[player]
    moves = []
    kind, _ = list(player) 

    if kind in ['D']:
        xmin, xmax = 2, 8
    else:
        xmin, xmax = -1, 11

    # Move out
    if position > 11:
        x = int(str(position)[0])
        for _x in range(x-1, xmin, -1): 
            if _x in (2, 4, 6, 8): 
                continue
            if state[_x] is not None:
                break
            moves.append(_x)
        
        for _x in range(x+1, xmax, 1):
            if _x in (2, 4, 6, 8):
                continue
            if state[_x] is not None:
                break
            moves.append(_x)
    
    # Move in
    else:
        goal = max([g for g in final_hallway[kind] if not state[g]])
        x0 = position
        x1 = int(str(goal)[0])

        if x0 > x1:
            xrange = range(x0-1, x1, -1)
        else:
            xrange = range(x0+1, x1)

        for _x in xrange:
            if state[_x] != None:
                break
        else:
            moves.append(goal)

    # Compute cost
    new_states = []
    for move in moves:
        new_state = state.copy()
        new_state[position] = None
        new_state[move] = player
        new_states.append([new_state, move_cost(player, position, move)])

    return new_states


def move_cost(player, x0, x1):
    
    cost = COST[list(player)[0]]

    steps = 0
    if x0 > 11:
        steps += 1 + int(str(x0)[1])
        x0 = int(str(x0)[0])
    if x1 > 11:
        steps += 1 + int(str(x1)[1])
        x1 = int(str(x1)[0])

    return (steps + abs(x1 - x0)) * cost


def possible_moves(state, cost, final_hallway):

    players = find_players_that_move(state, final_hallway)
    moves = []
    for player in players:
        for m in find_moves(state, cost, player, final_hallway):
                moves.append(m)

    return moves


def is_valid(state, final_hallway):

    if len(set([value for key, value in state.items() if key <= 11])) != 1:
        return False

    for kind, dest in final_hallway.items():
        for d in dest:
            if kind != str(state[d])[0]:
                return False

    return True


def state_tuple(state):
    keys = sorted(state.keys())
    return tuple([state[key] for key in keys])


def compute(state, final_hallway):
    
    risk = {state_tuple(state): [0, state]}
    dummy_risk = [0]

    while True:

        min_risk = min(dummy_risk) 
        dummy_risk.remove(min_risk)

        for stateid, (cost, state) in risk.items():
            if cost == min_risk:
                break
        else:
            continue

        risk.pop(stateid)
        m = possible_moves(state=state, cost=cost, final_hallway=final_hallway)

        if is_valid(state, final_hallway): 
            break

        for next_state, cost in m:
            nextid = state_tuple(next_state)
            if risk.get(nextid, [1E10, next_state])[0] > min_risk + cost:
                risk[nextid] = [min_risk + cost, next_state]
                dummy_risk.append(min_risk + cost)
    
    return min_risk 
 

if __name__ == '__main__':
    burrow, target = part1()
    solution = compute(burrow, target)
    print('Part1 solution: ', solution)
    assert solution == 19167

    burrow, target = part2()
    solution = compute(burrow, target)
    print('Part2 solution: ', solution)
    assert solution == 47665
