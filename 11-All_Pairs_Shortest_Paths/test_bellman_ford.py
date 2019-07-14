import pytest
from bellman_ford import bellman_ford

# Adjacency list of example graph from lectures
adj_list = {
    (1, 2): 1,
    (1, 3): 4,
    (2, 3): 2,
    (2, 4): 6,
    (3, 4): 3,
    }

n = 4
source_node = 1
expected = [0, 1, 3, 6]
t1 = (adj_list, n, source_node, expected)


adj_list = {
    (1, 2): 2, 
    (1, 3): 4, 
    (2, 3): 1,
    (2, 4): 2,
    (3, 5): 4,
    (4, 5): 2
}

n = 5
source_node = 1
expected = [0, 2, 3, 4, 6]
t2 = (adj_list, n, source_node, expected)

test_cases = [t1, t2]

@pytest.mark.parametrize('adj_list, n, source_node, expected', test_cases)
def test_dijkstra(adj_list, n, source_node, expected):
    actual = bellman_ford(adj_list, n, source_node)

    assert(expected == actual)