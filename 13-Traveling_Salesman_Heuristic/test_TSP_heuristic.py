import math
import pytest
from pathlib import Path
from TSP_heuristic import TSP_heuristic, read_input, read_output


path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course4\assignment3TSPHeuristic").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    vertex_labels, vertices, n = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (vertex_labels, vertices, n, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('vertex_labels, vertices, n, expected', test_cases)
def test_knapsack(vertex_labels, vertices, n, expected):
    actual = math.floor(TSP_heuristic(vertex_labels, vertices, n))

    assert(expected == actual)