import pytest
from compute_SCCs import *

#Reversed graph given as an example in the lectures
adj_list_rev = [[1,7], [2,5], [3,9], [4,1], [5,8], [6,3], [6,8], [7,4], [7,9], [8,2], [9,6]]

#Reverse the graph
adj_list = []
for i in adj_list_rev:
    adj_list.append(i[::-1])

t1 = (adj_list, 3)

test_cases = [t1]

@pytest.mark.parametrize('adj_list, expected', test_cases)
def test_kosaraju(adj_list, expected):
    number_of_SCCs = len(kosaraju(adj_list))

    assert(number_of_SCCs == expected)


file = open('SCC.txt')
adj_list = []
for line in file:
    adj_list.append([int(x) for x in line.split()])

t2 = (adj_list, [434821, 968, 459, 313, 211])

test_cases = [t2]

@pytest.mark.parametrize('adj_list, expected', test_cases)
def test_SCC_sizes(adj_list, expected):
    SCC_sizes = kosaraju(adj_list)
    sorted_SCC_sizes = sorted(SCC_sizes, reverse=True)

    assert(sorted_SCC_sizes[0:5] == expected)
    assert(sorted_SCC_sizes)