import sys
from antcolony import AntColony
from inputoutput import parseInput

class State:
    def __init__(self, Q, alpha, beta, numAnts, decay, maxIterations):
        self.Q = Q
        self.alpha = alpha
        self.beta = beta
        self.numAnts = numAnts
        self.decay = decay
        self.maxIterations = maxIterations

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <input_file>')
        sys.exit(1)
    isEuclidean, numCities, cities, DistMat = parseInput(sys.argv[1])

    # state = State(Q=5, alpha=1, beta=15, numAnts=100, decay=0.2, maxIterations=10)
    state = State(Q=5, alpha=1, beta=15, numAnts=300, decay=0.5, maxIterations=50)
    # state = State(Q=5, alpha=1, beta=-0.01, numAnts=300, decay=0.2, maxIterations=10)

    values = []
    for i in range(10):
        values.append(AntColony(numCities, DistMat, cities, state.Q, state.alpha, state.beta, state.numAnts, state.decay, state.maxIterations))
    print(f"State:({state.Q},{state.alpha},{state.beta},{state.numAnts},{state.decay},{state.maxIterations})",min(values))