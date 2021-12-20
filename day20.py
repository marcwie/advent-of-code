def load_data(filename):

    with open(filename) as infile:
        data = infile.read().splitlines()

    algorithm = data[0]
    image = data[2:]

    return algorithm, image


def extend_image(image, embedding=2):
    
    rows, cols = len(image), len(image[0])
    extend = 2 * embedding - 1
    embedded_image = [['.' * (cols + 2 * extend)] for _ in range(embedding)]

    for row in image:
        embedded_image.append(['.' * extend + row + '.' * extend])

    for _ in range(embedding):
        embedded_image.append(['.' * (cols + 2 * extend)])

    return embedded_image


#def enhance(image):
    
     

def run():

    algorithm, image = load_data(filename='data/day20/test')
    image = extend_image(image)
    print(image) 

if __name__ == '__main__':
    run()
