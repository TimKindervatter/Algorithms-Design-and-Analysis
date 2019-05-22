import pytest
from greedy_scheduling import *

t1 = ([[1,1], [2,1], [3,1]], [[3,1], [2,1], [1,1]])
t2 = ([[1,1], [1,2], [1,3]], [[1,1], [1,2], [1,3]])
t3 = ([[2,1], [3,2], [5,5]], [[3,2], [2,1], [5,5]])

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_difference(jobs, expected):
    schedule = greedy_difference(jobs)

    assert(schedule == expected)

t3 = ([[2,1], [3,2], [5,5]], [[2,1], [3,2], [5,5]])

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_ratio(jobs, expected):
    schedule = greedy_ratio(jobs)

    assert(schedule == expected)

t1 = ([[1,1], [2,1], [3,1]], 10, greedy_ratio)
t2 = ([[1,1], [1,2], [1,3]], 10, greedy_ratio)
t3 = ([[2,1], [3,2], [5,5]], 51, greedy_ratio)
t4 = ([[2,1], [3,2], [5,5]], 51, greedy_difference)

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('jobs, expected, f', test_cases)
def test_sum_weighted_completion_times(jobs, expected, f):
    schedule = f(jobs)
    sum = sum_weighted_completion_times(schedule)

    assert(sum == expected)