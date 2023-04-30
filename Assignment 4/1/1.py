from antcolony import AntColony
from inputoutput import parseInput
import sys
from antcolony import AntColony
import time

class State:
    def __init__(self, Q, alpha, beta, numAnts, decay, maxIterations):
        self.Q = Q
        self.alpha = alpha
        self.beta = beta
        self.numAnts = numAnts
        self.decay = decay
        self.maxIterations = maxIterations
 
if __name__ == '__main__':
    startTime = time.time()
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <input_file> ')
        sys.exit(1)
    isEuclidean, numCities, cities, DistMat = parseInput(sys.argv[1])

    minTour = []
    minTourDistance = sys.maxsize
    while time.time() - startTime < 150:
        tour, tourDistance = AntColony(numCities, DistMat, cities, Q = 4, alpha = 1, beta = 15, numAnt = 300, decay = 0.5, maxIterations = 15)
        if tourDistance < minTourDistance:
            minTour = tour
            minTourDistance = tourDistance

    print(f"Tour found is: {minTour}")
    print(f"Tour distance is: {minTourDistance}")
    # print(time.time() - startTime)
