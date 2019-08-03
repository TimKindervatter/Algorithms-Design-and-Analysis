def papadimitriou(n, clauses):
    non_negated = set()
    negated = set()
    for clause in clauses:
        for variable in clause:
            if variable > 0:
                non_negated.add(variable)
            elif variable < 0:
                negated.add(variable)

    removable_variables = non_negated.symmetric_difference(negated)
    
    for clause in clauses:
        for variable in clause:
            if abs(variable) in removable_variables:
                clauses.remove(clause)

    return len(clauses)


def read_input(filename):
    with open(filename) as f:
        n = f.readline()
        clauses = []
        for line in f.readlines():
            clauses.append([int(x) for x in line.split()])

    return n, clauses


if __name__ == '__main__':
    n, clauses = read_input('2sat2.txt')

    result = papadimitriou(n, clauses)