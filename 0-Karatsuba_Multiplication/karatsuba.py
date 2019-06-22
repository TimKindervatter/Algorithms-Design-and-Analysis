import math


def karatsuba(x, y):
    if (x < 10) or (y < 10):
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = math.ceil(n/2)

    a, b = split(x, m)
    c, d = split(y, m)

    first_term = karatsuba(a, c)
    third_term = karatsuba(b, d)
    second_term = karatsuba(a+b, c+d) - first_term - third_term

    return (10**(2*m))*first_term + (10**m)*second_term + third_term


def split(number, m):
    return number//(10**m), number % (10**m)