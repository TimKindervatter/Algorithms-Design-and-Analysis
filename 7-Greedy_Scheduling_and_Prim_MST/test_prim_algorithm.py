import pytest
from pathlib import Path
from prim_algorithm import prim

path = Path(__file__ + '../..').resolve()

data = []
with open(Path(path, "edges.txt")) as file:
    for line in file:
        data.append([int(x) for x in line.strip().split()])

adj_list = data[1:]

t1 = ([[1, 2, 1], [1, 3, 4], [1, 4, 3], [2, 4, 2], [3, 4, 5]], 7)
t2 = (adj_list, -3612829)

test_cases = [t1, t2]

@pytest.mark.parametrize('adj_list, expected', test_cases)
def test_prim(adj_list, expected):
    MST_cost = prim(adj_list)

    assert(MST_cost == expected)