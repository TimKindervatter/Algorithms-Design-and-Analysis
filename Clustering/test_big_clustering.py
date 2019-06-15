import pytest
from pathlib import Path
from big_clustering import big_cluster
from UnionFind import UnionFind

def read_input(filename):
    bitstrings = []
    with open(filename) as file:
        first_line = file.readline().split()
        num_nodes = int(first_line[0])
        n = int(first_line[1])
        for line in file.readlines():
            line = line.strip().replace(" ", "")
            bitstrings.append(line)

    return bitstrings, n


def read_output(filename):
    with open(filename) as file:
        number_of_clusters = int(file.readline())

    return number_of_clusters

path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course3\assignment2Clustering\question2").glob('**/*')
files = [x for x in path if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []

for i, _ in enumerate(input_files):
    bitstrings, n = read_input(input_files[0])
    expected = read_output(output_files[0])

    test_cases.append((bitstrings, n, expected))

@pytest.mark.parametrize('bitstrings, n, expected', test_cases)
def test_bit_clustering(bitstrings, n, expected):
    clusters = big_cluster(bitstrings, n)

    assert(len(clusters) == expected)
