import pytest
from UnionFind import UnionFind


#Union-Find is 1-indexed
t1 = ([x for x in range(1,7)], 3, 3)
t2 = ([x for x in range(1,7)], 0, 0)

test_cases = [t1, pytest.param(*t2, marks=pytest.mark.xfail)]

@pytest.mark.parametrize('nodes, x, expected', test_cases)
def test_find(nodes, x, expected):
    clusters = UnionFind(nodes)
    root = clusters.find(x)

    assert(root == expected)


t1 = ([x for x in range(1, 7)], 1, 4, {1:1, 2:2, 3:3, 4:1, 5:5, 6:6})
t2 = ([x for x in range(1, 7)], 4, 1, {1:4, 2:2, 3:3, 4:4, 5:5, 6:6})
t3 = ([x for x in range(1, 7)], 1, 1, {1:1, 2:2, 3:3, 4:4, 5:5, 6:6})

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('nodes, p, q, expected', test_cases)
def test_union(nodes, p, q, expected):
    clusters = UnionFind(nodes)
    clusters.union(p, q)

    new_parents = clusters.parent

    assert(new_parents == expected)


t1 = ('xyz', "[['x', 'y'], ['z']]")

test_cases = [t1]

@pytest.mark.parametrize('nodes, expected', test_cases)
def test_print(nodes, expected):
    clusters = UnionFind(nodes)
    clusters.union('x', 'y')
    string = clusters.__str__()

    assert(string == expected)


t1 = ('xyz', 2)

test_cases = [t1]

@pytest.mark.parametrize('nodes, expected', test_cases)
def test_len(nodes, expected):
    clusters = UnionFind(nodes)
    clusters.union('x', 'y')
    length = clusters.__len__()

    assert(length == expected)