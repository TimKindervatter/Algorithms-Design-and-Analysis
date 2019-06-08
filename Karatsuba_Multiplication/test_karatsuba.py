import pytest
from random import randint
from karatsuba import karatsuba

t0 = (34, 57, 1938)
t1 = (56, 12, 672)
t2 = (78, 34, 2652)
t3 = (56+78, 12+34, 6164)
t4 = (5678, 1234, 7006652)

#Answer to programming assignment
t5 = (2718281828459045235360287471352662497757247093699959574966967627,
        3141592653589793238462643383279502884197169399375105820974944592,
        8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)


random_tests = [(randint(-1e64, 1e64), randint(-1e64, 1e64)) for _ in range(100)]
random_tests = [random_tests[i] + (random_tests[i][0]*random_tests[i][1],) for i in range(len(random_tests))]

test_cases = [t0, t1, t2, t3, t4, t5] + random_tests

@pytest.mark.parametrize('x, y, expected', test_cases)
def test_karatsuba(x, y, expected):
    product = karatsuba(x, y)

    assert(product == expected)