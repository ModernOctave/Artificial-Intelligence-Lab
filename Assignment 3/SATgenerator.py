import sys
import random

class Literal:
    def __init__ (self, index, parity):
        self.index = index
        self.parity = parity


def Variable_Selector(n):

    Vars = [i for i in range(n)] 
    Arr = []

    for i in range(3):
        a = random.choice(Vars)
        Arr.append(a)
        Vars.remove(a)

    return Arr
    
def PrintClause(Clauses):

    inputFile = open("input.txt", 'w')

    for Clause in Clauses:

        inputFile.write("(")

        for Literal in Clause:

            if(Literal.parity):

                inputFile.write(f"x{Literal.index}")

            else:
                    
                inputFile.write(f"~x{Literal.index}")

            if Clause.index(Literal) != 2:
                inputFile.write("+")
            
        inputFile.write(")")
        
        inputFile.write('\n')
                






if __name__  == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: SATgenerator.py <number of variables> <number of clauses>")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    Clauses = []

    for i in range(k):
        Clause = []
        for j in Variable_Selector(n):
            Clause.append(Literal(j, random.choice([True, False])))
            
        Clauses.append(Clause)

    PrintClause(Clauses)

    
