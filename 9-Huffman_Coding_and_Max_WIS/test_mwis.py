import pytest
from pathlib import Path
import mwis


def read_input(filename):
    with open(filename) as f:
        num_weights = f.readline()
        weights = []
        for line in f.readlines():
            weights.append(int(line))

    return weights


def read_output(filename):
    with open(filename) as f:
        expected = f.readline().strip()

    return expected


filenames = Path(r'C:\Python\Stanford Algorithms Problem Sets\Test_Cases\stanford-algs\testCases\course3\assignment3HuffmanAndMWIS\question3').glob('**/*')
files = [x for x in filenames if x.is_file()]

input_files = [file for file in files if "input" in file.name]
output_files = [file for file in files if "output" in file.name]

test_cases = []
for i, _ in enumerate(input_files):
    input_filename = input_files[i]
    output_filename = output_files[i]

    test_cases.append((read_input(input_filename), read_output(output_filename)))


@pytest.mark.parametrize('weights, expected', test_cases)
def test_mwis(weights, expected):
    A = mwis.mwis(weights)
    S = mwis.reconstruct(A, weights)
    binary_string = mwis.make_binary_string(S)

    assert(binary_string == expected)


if __name__ == '__main__':
    weights = read_input(input_files[0])
    expected = read_output(output_files[0])

    A = mwis.mwis(weights)
    S = mwis.reconstruct(A, weights)
    binary_string = mwis.make_binary_string(S)

    print(binary_string)