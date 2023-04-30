import sys
from DFS import DFS
path = []

dirList = ['up','down','left','right']

def parseMaze(filename):
    f = open(filename, 'r')

    Graph = []
    for line in f:
        graphLine = []
        for char in line:
            if (char == ' '):
                graphLine.append(1)
            elif (char == '*'):
                graphLine.append(2)
            elif (char == '\n'):
                pass
            else:
                graphLine.append(0)
        Graph.append(graphLine)

    return Graph

def DFS_ExploreNode(x,y,prevDir,maze):
    if maze[x][y] == 2:
        return (True, [(x,y)])
    elif maze[x][y] == 1:
        for dir in dirList:
            if dir != prevDir:
                if dir == 'left':
                    if x-1 >= 0:
                        if maze[x-1][y] == 1:
                            (isFound, arr) = DFS_ExploreNode(x-1,y,dir)
                            if isFound:
                                return (True, arr.append((x,y)))
                            else:
                                return (False, arr)
                elif dir == 'right':
                    if x+1 < len(maze[0]):
                        if maze[x+1][y] == 0:
                            (isFound, arr) = DFS_ExploreNode(x+1,y,dir)
                            if isFound:
                                return (True, arr.append((x,y)))
                            else:
                                return (False, arr)
                elif dir == 'down':
                    if y+1 < len(maze):
                        if maze[x][y+1] == 0:
                            (isFound, arr) = DFS_ExploreNode(x,y+1,dir)
                            if isFound:
                                return (True, arr.append((x,y)))
                            else:
                                return (False, arr)
                elif dir == 'up':
                    if y-1 >= 0:
                        if maze[x][y-1] == 0:
                            (isFound, arr) = DFS_ExploreNode(x,y-1,dir)
                            if isFound:
                                return (True, arr.append((x,y)))
                            else:
                                return (False, arr)
    return (False, [])

def runDFS(maze):
    DFS_ExploreNode(0,0,'up',maze)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    
    maze = parseMaze(sys.argv[1])
    for x in maze:
        print(x)