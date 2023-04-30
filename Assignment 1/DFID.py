from DLDF import DLDF

class DFID:
    def __init__(self, graph):
        self.limit = 1
        self.graph = graph
        self.explored = []
        self.numExplored = 0
    
    def begin(self, x, y):
        complete = False
        while(not complete):
            if self.limit == 33:
                print("hi")
            myDLDF = DLDF(self.graph)
            complete = myDLDF.begin(0,0, self.limit)
            self.limit += 1
            self.numExplored += len(myDLDF.explored)
        
        self.myDLDF = myDLDF
        

    def filter(self):
        return self.myDLDF.filter()

    def getNumExplored(self):
        return self.numExplored

        
    
