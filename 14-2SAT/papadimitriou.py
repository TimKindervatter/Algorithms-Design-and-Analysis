import math
import random
from pathlib import Path


def papadimitriou(clauses):
    def evaluate_condition(variable):
        if variable > 0:
            return assignment[variable]
        elif variable < 0:
            return not assignment[abs(variable)]

    variables = set()
    for clause in clauses:
        for variable in clause:
            variables.add(abs(variable))

    n = len(variables)
    assignment = {}
    for _ in range(math.floor(math.log2(n))):
        for variable in variables:
            assignment[variable] = random.choice([True, False])

        for _ in range(2*n**2):
            all_clauses_satisfied = True
            unsatisfied_clauses = []
            for clause in clauses:
                this_clause_satisfied = evaluate_condition(clause[0]) or evaluate_condition(clause[1])
                all_clauses_satisfied &= this_clause_satisfied
                
                if not this_clause_satisfied:
                    unsatisfied_clauses.append(clause)
            
            if not all_clauses_satisfied:
                arbitrary_clause = random.choice(unsatisfied_clauses)
                variable_to_flip = abs(random.choice([arbitrary_clause[0], arbitrary_clause[1]]))
                assignment[variable_to_flip] = not assignment[variable_to_flip]
            else:
                return True

    return False


def reduce_clauses(clauses):
    """
    Preprocessing step for 2SAT to reduce the number of clauses that need to be checked.
    Loops over all clauses and sorts variables into two sets: non-negated and negated.
    Any variables which appear exclusively in one set or the other need not be checked.

    A variable which appears exclusively in the non-negated set can be set to True and all clauses 
    in which it appears will be satisfied. Similarly, any variable which appears exclusively in
    the negated set can be set to False, and any clause in which it appears will be satisfied.
    
    Arguments:
        clauses {list of lists} -- List containing sublists of length two whose elements are the two variables in the clause.
    
    Returns:
        reduced_clauses -- A set of clauses with all unneeded clauses removed.
    """
    removable_variables = [1]  # Dummy value to ensure while loop runs at least once

    while removable_variables:
        non_negated = set()
        negated = set()
        for clause in clauses:
            for variable in clause:
                if variable > 0:
                    non_negated.add(variable)
                elif variable < 0:
                    negated.add(abs(variable))

        # The set of all variables which appear exclusively in one set or the other is the symmetric difference of the two sets
        removable_variables = non_negated.symmetric_difference(negated)
        
        # Create a new list of clauses that excludes any clause which contains a removable variable
        new_clauses = []
        for clause in clauses:
            if not (abs(clause[0]) in removable_variables or abs(clause[1]) in removable_variables):
                new_clauses.append(clause)
                
        clauses = new_clauses

    return clauses


def read_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        clauses = []
        for line in f.readlines():
            clauses.append([int(x) for x in line.split()])

    return n, clauses


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()
    prefix = '2sat'
    filenames = [prefix + str(i) + '.txt' for i in range(1, 7)]
    for filename in filenames:
        n, clauses = read_input(Path(path, filename))

        reduced_clauses = reduce_clauses(clauses)
        result = papadimitriou(reduced_clauses)
        print(result)