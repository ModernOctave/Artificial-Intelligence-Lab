class DLDF:
    def __init__(self,graph):
        self.graph = graph
        self.dirList = ['left','right','up','down']
        self.frontier = []
        self.explored = []
        self.nodes = [[None for y in range(len(self.graph[0]))] for x in range(len(self.graph))]
        self.goal = None

    class Node:
        def __init__(node,x,y,prev = None, depth = 0):
            node.x = x
            node.y = y
            node.prev = prev
            node.depth = depth 


    def explore(self,x,y,limit):
        if self.graph[x][y] == 2:
            self.goal = self.nodes[x][y]
            self.explored.append(self.nodes[x][y])
            return True

        if self.nodes[x][y].depth < limit-1:
            for dir in self.dirList:
                if dir == 'left':
                    if y-1 >= 0:
                        if (self.graph[x][y-1] != 0) and (self.nodes[x][y-1] not in self.explored) and (self.nodes[x][y-1] not in self.frontier):
                            newNode = self.Node(x, y-1, self.nodes[x][y], self.nodes[x][y].depth + 1)
                            self.nodes[x][y-1] = newNode
                            self.frontier.append(newNode)
                elif dir == 'right':
                    if y+1 < len(self.graph[0]):
                        if (self.graph[x][y+1] != 0 and (self.nodes[x][y+1] not in self.explored) and (self.nodes[x][y+1] not in self.frontier)):
                            newNode = self.Node(x, y+1, self.nodes[x][y], self.nodes[x][y].depth + 1)
                            self.nodes[x][y+1] = newNode
                            self.frontier.append(newNode)
                elif dir == 'up':
                    if x-1 >= 0:
                        if (self.graph[x-1][y] != 0) and (self.nodes[x-1][y] not in self.explored) and (self.nodes[x-1][y] not in self.frontier):
                            newNode = self.Node(x-1, y, self.nodes[x][y], self.nodes[x][y].depth + 1)
                            self.nodes[x-1][y] = newNode
                            self.frontier.append(newNode)
                elif dir == 'down':
                    if x+1 < len(self.graph):
                        if (self.graph[x+1][y] != 0 and (self.nodes[x+1][y] not in self.explored) and (self.nodes[x+1][y] not in self.frontier)):
                            newNode = self.Node(x+1, y, self.nodes[x][y], self.nodes[x][y].depth + 1)
                            self.nodes[x+1][y] = newNode
                            self.frontier.append(newNode)

        self.explored.append(self.nodes[x][y])

        return False

    def begin(self,x,y,limit):
        newNode = self.Node(x,y)
        self.nodes[x][y] = newNode
        self.frontier.append(newNode)

        success = False

        while len(self.frontier) and not success:
            toExplore = self.frontier.pop()
            success = self.explore(toExplore.x,toExplore.y,limit)

        return success

    def filter(self):
        filter = [[None for y in range(len(self.graph[0]))] for x in range(len(self.graph))]
        pathLength = 1

        curNode = self.goal

        while curNode.prev:
            filter[curNode.x][curNode.y] = 1
            curNode = curNode.prev
            pathLength += 1

        filter[curNode.x][curNode.y] = 1

        return filter, pathLength