import pytest
from prim_algorithm import prim

t1 = ([[1, 2, 1], [1, 3, 4], [1, 4, 3], [2, 4, 2], [3, 4, 5]], 7)

test_cases = [t1]

@pytest.mark.parametrize('adj_list, expected', test_cases)
def test_prim(adj_list, expected):
    MST_cost = prim(adj_list)

    assert(MST_cost == expected)