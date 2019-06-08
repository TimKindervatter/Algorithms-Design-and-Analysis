import pytest
from random import randint
from karatsuba import karatsuba

t0 = (34, 57, 1938)
t1 = (56, 12, 672)
t2 = (78, 34, 2652)
t3 = (56+78, 12+34, 6164)
t4 = (5678, 1234, 7006652)

random_tests = [(randint(-1e64, 1e64), randint(-1e64, 1e64)) for _ in range(100)]
random_tests = [random_tests[i] + (random_tests[i][0]*random_tests[i][1],) for i in range(len(random_tests))]

test_cases = [t0, t1, t2, t3, t4] + random_tests

@pytest.mark.parametrize('x, y, expected', test_cases)
def test_karatsuba(x, y, expected):
    product = karatsuba(x, y)

    assert(product == expected)