import sys
from DFS import DFS
from BFS import BFS
from DFID import DFID

def parseMaze(filename):
    f = open(filename, 'r')

    Graph = []
    Raw = []
    isFirst = True


    for line in f:
        if (isFirst):
            FirstLine = int(line)
            isFirst = False
        else:
            graphLine = []
            rawLine = []
            for char in line:
                if (char == ' '):
                    graphLine.append(1)
                elif (char == '*'):
                    graphLine.append(2)
                elif (char == '\n'):
                    pass
                else:
                    graphLine.append(0)
                if (char != '\n'):
                    rawLine.append(char)
            Graph.append(graphLine)
            Raw.append(rawLine)

    return (FirstLine, Graph, Raw)

def printPath(filter, input):
    for x in range(len(input)):
        for y in range(len(input[0])):
            if filter[x][y]:
                print(0,end='')
            else:
                print(input[x][y],end='')
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    
    (FirstLine, maze, input) = parseMaze(sys.argv[1])
    
    if (FirstLine == 0):
        myMethod = BFS(maze)  
    elif (FirstLine == 1):
        myMethod = DFS(maze)
    elif(FirstLine == 2):
        myMethod = DFID(maze)
    
        
    myMethod.begin(0,0)

    (filter, pathLength) = myMethod.filter()

    print(myMethod.getNumExplored())
    print(pathLength)
    printPath(filter, input)