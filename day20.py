def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()

    algorithm = data[0]
    image = [list(row) for row in data[2:]]

    return algorithm, image


def extend_image(image, embedding=2):
    
    rows, cols = len(image), len(image[0])
    extend = 2 * embedding
    embedded_image = [['.'] * (cols + 2 * extend) for _ in range(extend)]

    for row in image:
        embedded_image.append(['.'] * extend + row + ['.'] * extend)

    for _ in range(extend):
        embedded_image.append(['.'] * (cols + 2 * extend))

    return embedded_image


def enhance_once(algorithm, image):
    
    row, col = len(image), len(image[0])
    enhanced = [] 
    enhanced.append(image[0])
    for i in range(1, row-1):
        enhanced_row = ['.']
        for j in range(1, col-1):
            number = [image[i+k][j+l] for k in range(-1,2) for l in range(-1,2)]
            number = ''.join(number).replace('.', '0').replace('#', '1')
            number = int(number, 2)
            enhanced_row.append(algorithm[number])
        enhanced_row.append('.')
        enhanced.append(enhanced_row)
    enhanced.append(image[-1])

    return enhanced


def crop(image):

    image = image[1:-1]
    image = [row[1:-1] for row in image]
    return image


def enhance(algorithm, image, n_steps):

    image = extend_image(image, embedding=n_steps)
    for _ in range(n_steps):
        image = crop(enhance_once(algorithm, image))

    return count_pixel(image)


def count_pixel(image):
    return sum([entry == '#' for row in image for entry in row])


def run():
    algorithm, image = load_data(filename='data/day20/test')
    solution = enhance(algorithm, image, n_steps=2) 
    assert solution == 35

    algorithm, image = load_data(filename='data/day20/input')
    solution = enhance(algorithm, image, n_steps=2) 
    print('Part1 solution:', solution)
    assert solution == 5057

    algorithm, image = load_data(filename='data/day20/test')
    solution = enhance(algorithm, image, n_steps=50) 
    assert solution == 3351

    algorithm, image = load_data(filename='data/day20/input')
    solution = enhance(algorithm, image, n_steps=50) 
    print('Part2 solution:', solution)
    assert solution == 18502


if __name__ == '__main__':
    run()
