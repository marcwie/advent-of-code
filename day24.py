A = [ 1,  1,  1,  1,  26,  1, 26,  1,  1,  26,  26, 26,  26,  26]
B = [15, 15, 12, 13, -12, 10, -9, 14, 13, -14, -11, -2, -16, -14]
C = [15, 10, 2, 16, 12, 11, 5, 16,  6, 15, 3, 12, 10, 13]


def chunk(w, z, a, b, c):
    #inp w
    #mul x 0
    #add x z
    #mod x 26
    x = z % 26
    
    #div z a1
    z = z // a 
    
    #add x 15
    x += b
    
    #eql x w
    #eql x 0
    x = int(x != w)

    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 25 * x + 1

    #mul y 0
    #add y w
    #add y 15
    #mul y x
    #add z y
    z += (w + c) * x
    
    return z


def compute(find):
    
    if find == 'max':
        f = max
        default = 0
    else:
        f = min
        default = 1E99

    states = {0: 0}
    
    for i in range(14):
        new_state = {}
        for z, v in states.items():
            for w in range(1, 10):
                next_z = chunk(w, z, A[i], B[i], C[i])
                _v = v + w * 10 ** (13 - i)
                new_state[next_z] = f((new_state.get(next_z, default), _v))

        states = new_state

    return states[0]


def run():
    
    print('Computing solutions. Takes a while...')

    solution = compute(find='max')
    print('Part1 solution:', solution)
    assert solution == 89959794919939

    solution = compute(find='min')
    print('Part2 solution:', solution)
    assert solution == 17115131916112


if __name__ == '__main__':
    run()
