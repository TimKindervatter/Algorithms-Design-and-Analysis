import pytest
from pathlib import Path
from huffman_coding import huffman, read_input, read_output


t1 = ([3, 2, 6, 8, 2, 6], [4,2])
t2 = ([60, 25, 10, 5], [3,1])

path = Path(r"C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course3\assignment3HuffmanAndMWIS\question1And2").glob('**/*')
files = [x for x in path if x.is_file()]
input_files = [file for file in files if 'input' in file.name]
output_files = [file for file in files if 'output' in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    test_cases.append((read_input(input_files[i]), read_output(output_files[i])))

test_cases = [t1, t2] + test_cases


@pytest.mark.parametrize('symbol_weights, expected', test_cases)
def test_huffman(symbol_weights, expected):
    symbol_tree = huffman(symbol_weights)

    max_depth = symbol_tree.max_depth
    min_depth = symbol_tree.min_depth

    assert(expected == [max_depth, min_depth])