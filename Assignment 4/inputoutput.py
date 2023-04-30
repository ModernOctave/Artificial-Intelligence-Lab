class Cities:
    def __init__(self, x, y, index):

        self.x = x
        self.y = y
        self.index = index

def parseInput(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

    # Parse the first line
    if lines[0] == 'euclidean':
        isEuclidean = True
    elif lines[0] == 'noneuclidean':
        isEuclidean = False
    else:
        raise Exception('Invalid input file')

    # Parse the second line
    numCities = int(lines[1])

    # Separate the rest of the lines
    coordinateLines = lines[2:2+numCities]
    distanceLines = lines[2+numCities:2+2*numCities]

    # Parse the city data
    DistMat = [[None for i in range(numCities)] for j in range(numCities)]
    for line in distanceLines:
        lineArr = line.split(' ')
        for entry in lineArr:
            DistMat[distanceLines.index(line)][lineArr.index(entry)] = float(entry)
    cities = []
    for line in coordinateLines:
        x, y = line.split(' ')
        cities.append(Cities(x, y, coordinateLines.index(line)))

    return isEuclidean, numCities, cities, DistMat