from asyncio import threads
import sys
import random
import concurrent.futures
from multiprocessing import Process, Array, Pool
from heapq import heappush, heappop
from inputoutput import parseInput
from antcolony import AntColony

class State:
    def __init__(self, Q, alpha, beta, numAnts, decay, maxIterations):
        self.Q = Q
        self.alpha = alpha
        self.beta = beta
        self.numAnts = numAnts
        self.decay = decay
        self.maxIterations = maxIterations

def moveGen(state):
    newStates = []

    choices = random.choices(['Q', 'alpha', 'beta', 'numAnts', 'decay', 'maxIterations'], k=2)
    newQ = state.Q
    newAlpha = state.alpha
    newBeta = state.beta
    newNumAnts = state.numAnts
    newDecay = state.decay
    newMaxIterations = state.maxIterations
    
    for i in range(3):
        if 'Q' == choices[0]:
            dQ = [-1,0,1]
            newQ = state.Q + dQ[i]
        elif 'alpha' == choices[0]:
            dalpha = [-0.1,0,0.1]
            newAlpha = state.alpha*(1+dalpha[i])
        elif 'beta' == choices[0]:
            dbeta = [-0.1,0,0.1]
            newBeta = state.beta*(1+dbeta[i])
        elif 'numAnts' == choices[0]:
            dnumAnts = [-1,0,1]
            newNumAnts = state.numAnts + dnumAnts[i]
        elif 'decay' == choices[0]:
            ddecay = [-0.1,0,0.1]
            newDecay = state.decay*(1+ddecay[i])
        elif 'maxIterations' == choices[0]:
            dmaxIterations = [-5,0,5]
            newMaxIterations = state.maxIterations + dmaxIterations[i]
        
        for j in range(3):
            if 'Q' == choices[1]:
                dQ = [-1,0,1]
                newQ = state.Q + dQ[j]
            elif 'alpha' == choices[1]:
                dalpha = [-0.1,0,0.1]
                newAlpha = state.alpha*(1+dalpha[j])
            elif 'beta' == choices[1]:
                dbeta = [-0.1,0,0.1]
                newBeta = state.beta*(1+dbeta[j])
            elif 'numAnts' == choices[1]:
                dnumAnts = [-1,0,1]
                newNumAnts = state.numAnts + dnumAnts[j]
            elif 'decay' == choices[1]:
                ddecay = [-0.1,0,0.1]
                newDecay = state.decay*(1+ddecay[j])
            elif 'maxIterations' == choices[1]:
                dmaxIterations = [-5,0,5]
                newMaxIterations = state.maxIterations + dmaxIterations[j]

            
            newState = State(newQ, newAlpha, newBeta, newNumAnts, newDecay, newMaxIterations)
            newStates.append(newState)

    return newStates

def AntColonyThread(numCities, DistMat, cities, Q, alpha, beta, numAnts, decay, maxIterations, array, index):
    array[index] = AntColony(numCities, DistMat, cities, Q, alpha, beta, numAnts, decay, maxIterations)

def HC(initialState):
    currState = initialState
    currValue = AntColony(numCities, DistMat, cities, currState.Q, currState.alpha, currState.beta, currState.numAnts, currState.decay, currState.maxIterations)

    while True:
        neighbours = moveGen(currState)
        values = Array('f', [1000000]*len(neighbours))
        threads = [Process(target=AntColonyThread, args=(numCities, DistMat, cities, neighbour.Q, neighbour.alpha, neighbour.beta, neighbour.numAnts, neighbour.decay, neighbour.maxIterations, values, neighbours.index(neighbour))) for neighbour in neighbours]
        for i, thread in enumerate(threads):
            thread.start()
        for thread in threads:
            thread.join()
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     for i, neighbour in enumerate(neighbours):
        #         values[i] = executor.submit(AntColony, numCities, DistMat, cities, neighbour.Q, neighbour.alpha, neighbour.beta, neighbour.numAnts, neighbour.decay, neighbour.maxIterations)
        # for i, value in enumerate(values):
        #     values[i] = value.result()
        values = values[:]
        minValue = min(values)

        if minValue <= currValue:
            currValue = minValue
            currState = neighbours[values.index(minValue)]
            print(currValue, f", State:({currState.Q},{currState.alpha},{currState.beta},{currState.numAnts},{currState.decay},{currState.maxIterations})")
        else:
            return currState, currValue

def BFS(initialState, target):
    currState = initialState
    currValue = AntColony(numCities, DistMat, cities, currState.Q, currState.alpha, currState.beta, currState.numAnts, currState.decay, currState.maxIterations)
    explored = []
    frontier = []

    while currValue > target:
        neighbours = moveGen(currState)
        neighbours = [x for x in neighbours if x not in explored and x not in frontier]
        threads = []

        pool = Pool()
        values = [None]*len(neighbours)
        for neighbour in neighbours:
            threads.append(pool.apply_async(AntColony, args=(numCities, DistMat, cities, neighbour.Q, neighbour.alpha, neighbour.beta, neighbour.numAnts, neighbour.decay, neighbour.maxIterations)))
        for i,neighbour in enumerate(neighbours):
            values[i] = threads[i].get()
        pool.close()
        pool.join()
        
        values = values[:]
        for i, neighbour in enumerate(neighbours):
            heappush(frontier,(values[i],neighbour))

        if values:
            currValue = AntColony(numCities, DistMat, cities, currState.Q, currState.alpha, currState.beta, currState.numAnts, currState.decay, currState.maxIterations)
            heappush(frontier, (currValue, currState))
        else:
            explored.append(currState)
        currValue, currState = heappop(frontier)
        print(currValue, f", State:({currState.Q},{currState.alpha},{currState.beta},{currState.numAnts},{currState.decay},{currState.maxIterations})")

        # if minValue <= currValue:
        #     currValue = minValue
        #     currState = neighbours[values.index(minValue)]
        #     print(currValue, f", State:({currState.Q},{currState.alpha},{currState.beta},{currState.numAnts},{currState.decay},{currState.maxIterations})")
        # else:
        #     return currState, currValue
    return currState, currValue


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <input_file>')
        sys.exit(1)
    isEuclidean, numCities, cities, DistMat = parseInput(sys.argv[1])
    
    # initialState = State(8, 1, 15, 100, 0.2, 10)
    initialState = State(8,0.81,9.8415,97,0.26462700000000006,20)
    # bestValue = 2000
    # while bestValue > 1550:
    #     bestState, bestValue = HC(initialState)
    #     initialState = bestState
    bestState, bestValue = BFS(initialState, 1550)
    print(bestValue, f", State:({bestState.Q},{bestState.alpha},{bestState.beta},{bestState.numAnts},{bestState.decay},{bestState.maxIterations})")