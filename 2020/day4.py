def load_data(filename):
    
    with open(filename) as infile:
        
        passports = infile.read().split('\n\n')
    
    passports = [p.replace('\n', ' ').split(' ') for p in passports]
        
    passport_dicts = []
    for p in passports:
        passport = {}
        if '' in p:
            p.remove('')
        for entry in p:
            key, value = entry.split(':')
            passport[key] = value

        passport_dicts.append(passport)

    return passport_dicts


def validate_naive(passport):
    
    keys = passport.keys()
    n_keys = len(keys)
    return (len(keys) == 8) or ((len(keys) == 7) and ('cid' not in keys))


def validate(passport):
    
    keys = passport.keys()
   
    # Check if all entries are present
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for required_key in required_keys:
        if required_key not in keys:
            return False

    # Check for correct entries in byr, iyr, eyr
    required_range = {'byr': (1920, 2002), 'iyr': (2010, 2020), 'eyr': (2020, 2030)}
    for key, allowed in required_range.items():
        entry = int(passport[key])
        if (entry < allowed[0]) or (entry > allowed[1]):
            return False
   
    # Check valid height
    hgt = passport['hgt']
    if hgt[-2:] == 'cm':
        hgt = int(hgt[:-2])
        if (hgt < 150) or (hgt > 193):
            return False
    elif hgt[-2:] == 'in':
        hgt = int(hgt[:-2])
        if (hgt < 59) or (hgt > 76):
            return False
    else:
        return False
    
    # Check hair color
    hcl = passport['hcl']
    if (hcl[0] != '#') or (len(hcl) != 7):
        return False
       
    # Check eye color
    ecl = passport['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    # Check pid
    pid = passport['pid']
    if len(pid) != 9:
        return False

    return True


def part1():

    passports = load_data(filename='data/day4/test')
    valid_passports = [validate_naive(p) for p in passports]
    solution = sum(valid_passports)
    assert solution == 2

    passports = load_data(filename='data/day4/input')
    valid_passports = [validate_naive(p) for p in passports]
    solution = sum(valid_passports)
    print('Part1 solution:', solution)


def part2():

    passports = load_data(filename='data/day4/test_part2')
    valid_passports = [validate(p) for p in passports]
    solution = sum(valid_passports)
    assert solution == 4

    passports = load_data(filename='data/day4/input')
    valid_passports = [validate(p) for p in passports]
    solution = sum(valid_passports)
    print('Part2 solution:', solution)


if __name__ == '__main__':
    part1()
    part2()


