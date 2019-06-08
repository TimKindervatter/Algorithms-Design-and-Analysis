import pytest
from karatsuba import karatsuba

t0 = (34, 57, 1938)
t1 = (56, 12, 672)
t2 = (78, 34, 2652)
t3 = (56+78, 12+34, 6164)
t4 = (5678, 1234, 7006652)

test_cases = [t0, t1, t2, t3, t4]

@pytest.mark.parametrize('x, y, expected', test_cases)
def test_karatsuba(x, y, expected):
    product = karatsuba(x, y)

    assert(product == expected)