import pytest
from UnionFind import UnionFind


#Union-Find is 1-indexed
t1 = ({1:1, 2:1, 3:1, 4:4, 5:4, 6:4}, {1:1, 2:0, 3:0, 4:1, 5:0, 6:0}, 3, 1)
t2 = ({1:1, 2:1, 3:1, 4:4, 5:4, 6:4}, {1:1, 2:0, 3:0, 4:1, 5:0, 6:0}, 4, 4)

test_cases = [t1, t2]

@pytest.mark.parametrize('parents, ranks, x, expected', test_cases)
def test_find(parents, ranks, x, expected):
    clusters = UnionFind(parents, ranks)
    root = clusters.find(x)

    assert(root == expected)


t1 = ({1:1, 2:1, 3:1, 4:4, 5:4, 6:4}, {1:1, 2:0, 3:0, 4:1, 5:0, 6:0}, 1, 4, {1:1, 2:1, 3:1, 4:1, 5:4, 6:4})

test_cases = [t1]

@pytest.mark.parametrize('parents, ranks, p, q, expected', test_cases)
def test_union(parents, ranks, p, q, expected):
    clusters = UnionFind(parents, ranks)
    new_parents = clusters.union(p, q)

    assert(new_parents == expected)