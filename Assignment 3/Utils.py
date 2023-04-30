from SATgenerator import Literal

digits = ['0','1','2','3','4','5','6','7','8','9']



def ParseFile(filename):
    Clauses = []
    NumVars = 0

    file = open(filename, "r")
    
    for line in file:
        line = line.strip('\n')
        isNegated = False
        number = None
        num = []
        Clause = []


        for char in line:
            if char == '~':
                isNegated = True
            
            if char == 'x':
                pass    
            
            if char in digits:
                num.append(char)

            if char == '+' or char == ')':
                number = int(''.join(num))
                if number > NumVars:
                    NumVars = number
                num = []
                newLiteral = Literal(number, not isNegated)
                Clause.append(newLiteral)
                isNegated = False

        Clauses.append(Clause)
 
    return Clauses, NumVars+1