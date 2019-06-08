import math


def karatsuba(x, y):
    x = str(x)
    y = str(y)

    if len(x) < len(y):
        x = '0' + x
    if len(y) < len(x):
        y = '0' + y

    if len(x) == 1 or len(y) == 1:
        return int(x)*int(y)

    n = min(len(x), len(y))
    m = n//2 if (n != 3) else 2

    a = first_half(x)
    b = second_half(x)
    c = first_half(y)
    d = second_half(y)

    product1 = karatsuba(a, c)
    product3 = karatsuba(a+b, c+d)
    product2 = karatsuba(b, d)
    
    first_term = product1
    second_term = product3 - product2 - product1
    third_term = product2

    return (10**(2*m))*first_term + (10**m)*second_term + third_term


def first_half(number):
    n = len(str(number))
    return int(str(number)[:n//2])


def second_half(number):
    n = len(str(number))
    return int(str(number)[n//2:])


if __name__ == '__main__':
    print(karatsuba(5678, 1234))