import pytest
from greedy_scheduling import *

t1 = ([[1,1], [2,1], [3,1]], [[3,1], [2,1], [1,1]])
t2 = ([[1,1], [1,2], [1,3]], [[1,1], [1,2], [1,3]])

test_cases = [t1, t2]

@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_difference(jobs, expected):
    schedule = greedy_difference(jobs)

    assert(schedule == expected)


@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_ratio(jobs, expected):
    schedule = greedy_ratio(jobs)

    assert(schedule == expected)