import math
import pytest
from pathlib import Path
from traveling_salesman import traveling_salesman, read_input, read_output


path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course4\assignment2TSP").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    vertices, n = read_input(input_files[i])
    expected = read_output(output_files[i])
    test_case = (vertices, n, expected)
    test_cases.append(test_case)


@pytest.mark.parametrize('vertices, n, expected', test_cases)
def test_knapsack(vertices, n, expected):
    actual = math.floor(traveling_salesman(vertices, n))

    assert(expected == actual)


if __name__ == '__main__':
    # vertices, n = read_input(input_files[92])
    # expected = read_output(output_files[92])

    path = Path(__file__ + "../..").resolve()
    vertices, n = read_input(Path(path, "test1.txt"))
    expected = 10
    actual = math.floor(traveling_salesman(vertices, n))

    print("Expected: " + str(expected))
    print("Actual: " + str(actual))