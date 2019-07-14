import pytest
from pathlib import Path
from floyd_warshall import floyd_warshall, read_input, read_output
from johnson import johnson


adj_list = {
    (1, 2): -2,
    (1, 3): 4,
    (2, 3): -1,
    (3, 4): 2,
    (3, 5): -3,
    (6, 4): 1,
    (6, 5): -4
}

n = 6
source_node = 0
expected = -6
t1 = (adj_list, n, expected)


path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course4\assignment1AllPairsShortestPath").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = [t1]
for i, _ in enumerate(input_files):
    adj_list, n = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (adj_list, n, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('adj_list, n, expected', test_cases)
def test_knapsack(adj_list, n, expected):
    source_node = 0
    actual = johnson(adj_list, n, source_node)

    assert(expected == actual)