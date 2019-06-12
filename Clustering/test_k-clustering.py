import pytest
from k_clustering import cluster

adj_list = [
    [1, 2, 10], [1, 3, 12], [1, 4, 6], [1, 5, 11.2], [1, 6, 13],
    [2, 3, 2], [2, 4, 11.7], [2, 5, 5], [2, 6, 5.4],
    [3, 4, 13.4], [3, 5, 5.4], [3, 6, 5],
    [4, 5, 10.05], [4, 6, 12.05],
    [5, 6, 2]]

t1 = (adj_list, 6, 3, 6)

test_cases = [t1]

@pytest.mark.parametrize('adj_list, n, k, expected', test_cases)
def test_cluster(adj_list, n, k, expected):
    clusters = cluster(adj_list, n, k)

    assert(clusters == expected)