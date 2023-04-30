# Main Program
## Usage
Usage: python3 1.py <filename> <method code> [Beam Width | Tabu Tenure]

<filename>
    Name of the input file (Use input generator to generate it)

<method code>
    Choose the method code from the following table
        0 - Beam Search
        1 - VND
        2 - Tabu Search

Optional Argument
    Beam Width
        If Beam Search is selected, beam width can be passed as the optional argument. If not specified, (Number of Variables)/2 will be taken by default.

    Tabu Tenure
        If Tabu Search is selected, tabu tenure can be passed as the optional argument. If not specified, (Number of Variables)^0.5 will be taken by default.
        
    Note: Only one Optional Argument should be given!

# Input Generator
## Brief
Generate the input file with the default name as input.txt

## Usage
Usage: SATgenerator.py <number of variables> <number of clauses>

<number of variables>
    This parameter specifies the number of input variables which can be used for generating the clauses.

<number of clauses>
    This parameter specifies the number of clauses that will be present in the boolean expression generated in the input.txt file.

## Format of Input.txt
Each line represents a clause and literals are added together to form a clause. Each literal is named as "xi" where i represents the index of the literal. index starts from 0 .Negated literals have a preceeding "~".

Example:
    (x3+x2+~x1)
    (x1+x3+~x0)
    (x2+x3+~x0)
    (~x2+x0+x1)
    (x1+x2+x3)