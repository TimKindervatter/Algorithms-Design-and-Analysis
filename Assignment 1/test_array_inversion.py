import pytest
from array_inversion import *

#Example array from lectures
t1 = ([1,3,5,2,4,6], 3)

#Answer to Assignment 1
with open('IntegerArray.txt') as text_file:
    array = []
    for line in text_file:
        array.append(int(line))
t2 = (array, 2407905288)

test_cases = [t1, t2]

@pytest.mark.parametrize('array, expected', test_cases)
def test_count_inversions(array, expected):
    number_of_inversions = count_inversions(array)

    assert(number_of_inversions == expected)