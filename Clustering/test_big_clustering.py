import pytest
from UnionFind import UnionFind

t1 = (["000", "001" "010" "011", "100", "101", "110", "111"], 3, 1, None)

test_cases = [t1]

@pytest.mark.parametrize('bitstrings, n, k, expected', test_cases)
def test_bit_clustering(bitstrings, n, k, expected):
    pass