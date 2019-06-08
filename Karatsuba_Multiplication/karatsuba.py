import math


def karatsuba(x, y):
    if (x < 0) ^ (y < 0):
        negative = True
    else:
        negative = False

    x = str(abs(x))
    y = str(abs(y))

    if len(x) < len(y):
        x = '0'*(len(y) - len(x)) + x
    if len(y) < len(x):
        y = '0'*(len(x) - len(y)) + y

    if len(x) == 1 or len(y) == 1:
        return int(x)*int(y)

    n = min(len(x), len(y))
    m = math.ceil(n/2) if (n != 3) else 2

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

    result = (10**(2*m))*first_term + (10**m)*second_term + third_term

    if negative:
        return -result
    else:
        return result


def first_half(number):
    n = len(str(number))
    return int(str(number)[:n//2])


def second_half(number):
    n = len(str(number))
    return int(str(number)[n//2:])


if __name__ == '__main__':
    print(karatsuba(11708, 90505))