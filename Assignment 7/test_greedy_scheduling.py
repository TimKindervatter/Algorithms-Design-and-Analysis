import pytest
from greedy_scheduling import *

t1 = ([[1,1], [2,1], [3,1]], [[3,1], [2,1], [1,1]]) #Example from lecture, each job has same length
t2 = ([[1,1], [1,2], [1,3]], [[1,1], [1,2], [1,3]]) #Example from lecture, each job has same weight
t3 = ([[2,1], [3,2], [5,5]], [[3,2], [2,1], [5,5]]) #Tie breaker test for greedy difference algorithm

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_difference(jobs, expected):
    schedule = greedy_difference(jobs)

    assert(schedule == expected)

t3 = ([[2,1], [3,2], [5,5]], [[2,1], [3,2], [5,5]]) #Greedy ratio will schedule these jobs differently than greedy difference

test_cases = [t1, t2, t3]

@pytest.mark.parametrize('jobs, expected', test_cases)
def test_greedy_ratio(jobs, expected):
    schedule = greedy_ratio(jobs)

    assert(schedule == expected)

t1 = ([[1,1], [2,1], [3,1]], 10, greedy_ratio)
t2 = ([[1,1], [1,2], [1,3]], 10, greedy_ratio)
t3 = ([[2,1], [3,2], [5,5]], 51, greedy_ratio)
t4 = ([[2,1], [3,2], [5,5]], 52, greedy_difference)

data = []
with open('jobs.txt') as f:
    for line in f.readlines():
        data.append([int(x) for x in line.strip().split()])

jobs = data[1:] #First line is number of jobs, not needed

#Answer to assignment 7, part 1
t5 = (jobs, 69119377652, greedy_difference)
#Answer to assignment 7, part 2
t6 = (jobs, 67311454237, greedy_ratio)

test_cases = [t1, t2, t3, t4, t5, t6]

@pytest.mark.parametrize('jobs, expected, f', test_cases)
def test_sum_weighted_completion_times(jobs, expected, f):
    schedule = f(jobs)
    sum = sum_weighted_completion_times(schedule)

    assert(sum == expected)