SIGN = [[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]]
ORDER = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]


def load_data(filename):
    
    scanners = []
    with open(filename) as infile:
        data = infile.read().splitlines()

    for line in data:
        if '---' in line:
            scanner = []
        elif ',' in line:
            scanner.append([int(p) for p in line.split(',')])
        else:
            scanners.append(scanner)
        
    if line != '':
        scanners.append(scanner)

    return scanners


def manhattan(x0, x1):
    return sum([abs(x0[i] - x1[i]) for i in range(len(x0))])

        
def euclidian(x1, x2):
    return sum([(x1[i] - x2[i]) ** 2 for i in range(len(x1))])


def distance(points):
    return [[euclidian(x1, x2) for x1 in points] for x2 in points]
    

def common_distances(distances1, distances2):
    unique_distances1 = set([d for row in distances1 for d in row]) - set([0])
    unique_distances2 = set([d for row in distances2 for d in row]) - set([0])
    return unique_distances1.intersection(unique_distances2)
 

def transform(point, order, sign):
    point = [point[o] for o in order]
    for s in sign:
        point[s] *= -1
    return point


def direction(x0, x1):
    return [x1[i] - x0[i] for i in range(len(x0))]


def common_beacons(scanner1, scanner2, min_overlap):
    
    distances1 = distance(scanner1)
    distances2 = distance(scanner2)

    common = common_distances(distances1, distances2)
    n_beacon1, n_beacon2 = len(scanner1), len(scanner2)

    beacon_pair1 = [[i, j] for c in common for i in range(n_beacon1) for j in range(i) if distances1[i][j] == c]
    beacon_pair2 = [[i, j] for c in common for i in range(n_beacon2) for j in range(i) if distances2[i][j] == c]
    
    n_common1 = len(set([i for pair in beacon_pair1 for i in pair]))
    n_common2 = len(set([i for pair in beacon_pair2 for i in pair]))
    
    if (n_common1 == n_common2) and (n_common1 >= min_overlap):
        return[[p1, p2] for p1, p2 in zip(beacon_pair1, beacon_pair2)]
    else:
        return None
      

def find_transformation(pairs, scanner1, scanner2):
    
    valid_transformation = [[s, o] for s in SIGN for o in ORDER]
    
    for p1, p2 in pairs[:1]:
        current_transforms = []
        x01, x11 = scanner1[p1[0]], scanner1[p1[1]]
        points2 = [(scanner2[p2[0]], scanner2[p2[1]]), (scanner2[p2[1]], scanner2[p2[0]])]
        i = 0
        for x02, x12 in points2:
            for s, o in valid_transformation:
                if direction(transform(x02, o, s), transform(x12, o, s)) == direction(x01, x11):
                    current_transforms.append([s, o])
                i += 1
        valid_transformation = current_transforms
    
    if len(valid_transformation):
        return valid_transformation
    else:
        return None


def map_scanners(scanner1, scanner2, sign, order, pairs):
    scanner2 = [transform(b, order, sign) for b in scanner2]
    
    offsets = []
    for p1, p2 in pairs:
        x01, x11 = scanner1[p1[0]], scanner1[p1[1]]
        points2 = [(scanner2[p2[0]], scanner2[p2[1]]), (scanner2[p2[1]], scanner2[p2[0]])]
        for x02, x12 in points2:
            if direction(x01, x11) == direction(x02, x12):
                offsets.append(direction(x02, x01))
                offsets.append(direction(x12, x11))

    position = []
    for i in range(3):
        o = set([d[i] for d in offsets])
        if len(o) > 1:
            return None
        position.append(o.pop())

    x0, y0, z0 = position
    scanner2 = [[x + x0, y + y0, z + z0] for x, y, z in scanner2]
    
    return scanner2, position 


def compute_positions(scanners):

    needs_adjustment = [False] + [True] * len(scanners[1:])
    scanner_positions = [[0, 0, 0]] 
    n_scanner = len(scanners)

    while sum(needs_adjustment):

        comb = ((i, j) for i in range(n_scanner) for j in range(n_scanner))

        for i, j in comb: 
            if needs_adjustment[i] or not needs_adjustment[j]:
                continue

            pairs = common_beacons(scanners[i], scanners[j], min_overlap=12)
            if not pairs:
                continue

            transformation = find_transformation(pairs, scanners[i], scanners[j])
            if not transformation:
                continue

            mappings =  [map_scanners(scanners[i], scanners[j], s, o, pairs) for s, o in transformation]
            mappings = [mapping for mapping in mappings if mapping]
            scanners[j] = mappings[0][0]
            scanner_positions.append(mappings[0][1])
            needs_adjustment[j] = False
    
    return scanners, scanner_positions


def unique_beacons(scanners):
    
    beacons = []
    for scanner in scanners:
        for position in scanner:
            if position not in beacons:
                beacons.append(position)

    return beacons


def n_unique_beacons(scanners):
    scanners, _ = compute_positions(scanners)
    return len(unique_beacons(scanners))


def largest_distance(scanners):
    _, pos = compute_positions(scanners)
    n_pos = range(len(pos))
    return max([manhattan(pos[i], pos[j]) for i in n_pos for j in n_pos])


def run():
    scanners = load_data(filename='data/day19/test')
    solution = n_unique_beacons(scanners)
    assert solution == 79

    scanners = load_data(filename='data/day19/input')
    solution = n_unique_beacons(scanners)
    print('Part1 solution:', solution)
    assert solution == 315

    scanners = load_data(filename='data/day19/test')
    solution = largest_distance(scanners)
    assert solution == 3621

    scanners = load_data(filename='data/day19/input')
    solution = largest_distance(scanners)
    print('Part2 solution:', solution)
    assert solution == 13192


if __name__ == '__main__':
    run()
