import pytest
from prim_algorithm import *



def test_find_MST(graph, expected):
    tree = find_MST(graph)

    assert(tree == expected)