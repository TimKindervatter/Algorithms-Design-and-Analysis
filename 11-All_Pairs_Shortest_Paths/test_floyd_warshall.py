import pytest
from pathlib import Path
from floyd_warshall import floyd_warshall, read_input, read_output

path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course4\assignment1AllPairsShortestPath").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    adj_list, n = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (adj_list, n, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('adj_list, n, expected', test_cases)
def test_knapsack(adj_list, n, expected):
    actual = floyd_warshall(adj_list, n)

    assert(expected == actual)