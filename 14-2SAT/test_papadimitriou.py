import math
import pytest
from pathlib import Path
from papadimitriou import papadimitriou, reduce_clauses, read_input, read_output


path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course4\assignment4TwoSat").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    clauses = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (clauses, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('clauses, expected', test_cases)
def test_knapsack(clauses, expected):
    reduced_clauses = reduce_clauses(clauses)
    actual = papadimitriou(reduced_clauses)

    assert(expected == actual)


if __name__ == '__main__':
    clauses, expected = test_cases[21]
    test_knapsack(clauses, expected)