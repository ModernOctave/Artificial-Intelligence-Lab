#            AI Lab 3
#           IIT Dharwad
#    
#             Group 1:
#       Om Patil (200010036)
#     Hrishikesh Pable (200010037)

import sys
from Utils import ParseFile
import itertools
import math

Clauses = []
NumVars = 0
goalState = None

def GoalTest(State):
    global Clauses

    FullSatisfied = True

    for Clause in Clauses:

        ClauseSatisfied = False

        for literal in Clause:

            if literal.parity == State[literal.index]:
                ClauseSatisfied = True
                break

        if not ClauseSatisfied:
            FullSatisfied = False
            break

    return FullSatisfied

def numSat(State):
    global Clauses

    numSat = 0

    for Clause in Clauses:

        ClauseSatisfied = False

        for literal in Clause:

            if literal.parity == State[literal.index]:
                ClauseSatisfied = True
                break

        if ClauseSatisfied:
            numSat += 1

    return numSat

def Beam(BeamSize, StartState):
    global Clauses, goalState

    def MoveGen(State):
        newStates = []

        for variable in State:

            newState = State.copy()
            
            newState[State.index(variable)] = not State[State.index(variable)]

            newStates.append(newState)

        return newStates

    Explored = []
    Beam = [StartState]

    goalFound = False

    while Beam and not goalFound:
        Frontier = []
        
        for State in Beam:

            if GoalTest(State):
                goalState = State
                goalFound = True
                Explored.append(goalState)
                break

            for newState in MoveGen(State):
                
                if newState not in Explored and newState not in Frontier:

                    Frontier.append(newState)

            Explored.append(State)
     
        Frontier.sort(reverse=True, key=numSat)

        Beam = Frontier[0:BeamSize-1]

    if goalFound:
        print("Goal state found!")
        print(goalState)
        print(f"Number of Explored States: {len(Explored)}")
    else:
        print("No goal state found!")

    
def VND(StartState):
    global Clauses, goalState
    density = 1

    def MoveGen(State):
        nonlocal density

        def MoveGenDensity(State, density):

            for comb in itertools.combinations(list(range(NumVars)), density):

                newState = State.copy()
                
                for index in comb:
                    newState[index] = not newState[index]
                    
                if newStates not in Explored:
                    newStates.append(newState)

            return newStates

        newStates = []

        while not newStates and density <= NumVars:
            newStates = MoveGenDensity(State, density)
            density += 1
     
        return newStates

    Explored = []
    goalFound = False
    nextState = StartState

    while nextState and not goalFound:
        if GoalTest(nextState):
            goalState = nextState
            goalFound = True
            Explored.append(goalState)
            break

        Frontier = MoveGen(nextState)

        Frontier.sort(reverse=True, key=numSat)

        Explored.append(nextState)

        if Frontier:
            nextState = Frontier[0]
        else:
            nextState = None

    if goalFound:
        print("Goal state found!")
        print(goalState)
        print(f"Number of Explored States: {len(Explored)}")
    else:
        print("No goal state found!")

def Tabu(StartState, Tenure):
    global Clauses, goalState

    CurrentTenure = [0] * NumVars

    def MoveGen(State):
        TenureDict = {}
        newStates = []
        nonlocal CurrentTenure

        CurrentTenure = [max(var-1, 0) for var in CurrentTenure]
            

        for variable in State:
        
            if (CurrentTenure[State.index(variable)]):
                continue

            newState = State.copy()
            
            newState[State.index(variable)] = not State[State.index(variable)]

            # key = str(newState)
            # value = 'asdf'

            value = CurrentTenure.copy()

            # if(CurrentTenure[State.index(variable)] == 0):

            value[State.index(variable)] = Tenure


            TenureDict[str(newState)] =  value
            
            newStates.append(newState)

        return newStates, TenureDict

    Explored = []
    goalFound = False
    nextState = StartState

    while nextState and not goalFound and len(Explored) < 5000:
        if GoalTest(nextState):
            goalState = nextState
            goalFound = True
            Explored.append(goalState)
            break

        Frontier, TenureDict = MoveGen(nextState)

        Frontier.sort(reverse=True, key=numSat)

        Explored.append(nextState)

        if Frontier:
            nextState = Frontier[0]
            CurrentTenure = TenureDict[str(Frontier[0])]
        else:
            nextState = None

    if goalFound:
        print("Goal state found!")
        print(goalState)
        print(f"Number of Explored States: {len(Explored)}")
    else:
        print("No goal state found!")    

if __name__ == '__main__':
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: python3 main.py <filename> <method code> [optional argument]")
        print("See README for more details")
        exit(1)
    
    Clauses, NumVars = ParseFile(sys.argv[1])

    StartState = [False] * NumVars

    if len(sys.argv) == 4 and sys.argv[3]:
        if sys.argv[2] == "0":
            Beam(int(sys.argv[3]) , StartState)
        elif sys.argv[2] == "1":
            VND(StartState)
        elif sys.argv[2] == "2":
            Tabu(StartState, int(sys.argv[3]))
    else:
        if sys.argv[2] == "0":
            Beam(math.floor(NumVars/2) , StartState)
        elif sys.argv[2] == "1":
            VND(StartState)
        elif sys.argv[2] == "2":
            Tabu(StartState, int(NumVars**0.5))
        