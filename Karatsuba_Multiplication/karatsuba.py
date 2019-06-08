def karatsuba(x, y):
    length_x = len(str(x))
    length_y = len(str(y))

    if length_x == 1 or length_y == 1:
        return x*y

    n = max(length_x, length_y)

    a = first_half(x)
    b = second_half(x)
    c = first_half(y)
    d = second_half(y)

    product1 = karatsuba(a, c)
    product2 = karatsuba(b, d)
    product3 = karatsuba(a+b, c+d)
    
    first_term = product1
    second_term = product3 - product2 - product1
    third_term = product2

    return (10**n)*first_term + (10**(n//2))*second_term + third_term


def first_half(number):
    n = len(str(number))
    return int(str(number)[:n//2])


def second_half(number):
    n = len(str(number))
    return int(str(number)[n//2:])


if __name__ == '__main__':
    karatsuba(1234, 5678)