import random
import copy
import numpy as np
import time
import sys

def AntColony(numCities,distances,cities,Q = 8, alpha = 1, beta = 15, numAnt = 300, decay = 0.2, maxIterations = 10):
    pheromone = [[1 for i in range(numCities)] for j in range(numCities)]
    
    def ant(pheromone, deltaPheromone):
        nonlocal distances, cities, Q, alpha, beta

        currentCity = cities[0]
        toVisitCities = copy.deepcopy(cities[1:])
        tourDistance = 0
        tour = [currentCity]

        def goToNextCity():
            nonlocal cities, toVisitCities, currentCity, tourDistance, tour
            weights = [pheromone[currentCity.index][i.index]**alpha/distances[currentCity.index][i.index]**beta for i in toVisitCities]
            nextCity = random.choices(toVisitCities, weights=weights)
            toVisitCities.remove(nextCity[0])
            tourDistance += distances[currentCity.index][nextCity[0].index]
            tour.append(nextCity[0])
            currentCity = nextCity[0]

        while len(toVisitCities) > 0:
            goToNextCity()

        for i in range(len(tour)-1):
            deltaPheromone[tour[i].index][tour[i+1].index] += Q/tourDistance
            deltaPheromone[tour[i+1].index][tour[i].index] += Q/tourDistance
        deltaPheromone[tour[-1].index][tour[0].index] += Q/tourDistance
        deltaPheromone[tour[0].index][tour[-1].index] += Q/tourDistance

        return tour, tourDistance

    def iteration():
        nonlocal pheromone, cities, numAnt, decay
        deltaPheromone = [[0]*numCities]*numCities
        tours = []
        tourDistances = []
        for i in range(numAnt):
            tour, tourDistance = ant(pheromone, deltaPheromone)
            tours.append(tour)
            tourDistances.append(tourDistance)

        pheromone = np.array(pheromone)
        pheromone = pheromone*(1-decay)
        pheromone += deltaPheromone

        minTourDistance = min(tourDistances)
        minTour = tours[tourDistances.index(minTourDistance)]

        return minTour, minTourDistance

    minimum = sys.maxsize
    start_time = time.time()
    while time.time() - start_time < 140:
        minTour, minTourDistance = iteration()
        minimum = min(minimum, minTourDistance)
        if minTourDistance == minimum:
            lastChange = 0

    minTour = [city.index for city in minTour]

    return minTour, minTourDistance
