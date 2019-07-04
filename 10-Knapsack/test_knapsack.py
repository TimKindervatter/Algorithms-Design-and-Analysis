import pytest
from pathlib import Path
from knapsack import knapsack, read_input, read_output

path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course3\assignment4Knapsack").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    knapsack_capacity, items = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (knapsack_capacity, items, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('knapsack_capacity, items, expected', test_cases)
def test_knapsack(knapsack_capacity, items, expected):
    actual = knapsack(knapsack_capacity, items)

    assert(expected == actual)


if __name__ == '__main__':
    knapsack_capacity = 6
    items = [[3, 4], [2, 3], [4, 2], [4, 3]]
    expected = 8
    test_case = (knapsack_capacity, items, expected)
    test_knapsack(*test_case)
    # test_knapsack(*test_cases[10])