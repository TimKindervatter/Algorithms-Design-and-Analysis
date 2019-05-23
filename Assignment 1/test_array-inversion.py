import pytest
from array_inversion import *

t1 = ([1,3,5,2,4,6], 3) #Example array from lectures

test_cases = [t1]

@pytest.mark.parametrize('array, expected', test_cases)
def test_count_split_inversions(array, expected):
    number_of_inversions = count_split_inversions(array)

    assert(number_of_inversions == expected)