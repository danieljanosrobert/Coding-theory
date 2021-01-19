from math import isqrt


def check_n(n):
    if n % 2 == 0:
        raise Exception('n nem paratlan. Fermat faktorizalas pozitiv paratlan szamokra mukodik.')
    if n < 0:
        raise Exception('n negativ. Fermat faktorizalas pozitiv paratlan szamokra mukodik.')


def fermat(n):
    check_n(n)
    a = isqrt(n)
    b = isqrt(n)
    while b * b != a * a - n:
        a = a + 1
        b = isqrt(a * a - n)
    p = a + b
    q = a - b
    assert n == p * q
    return p, q


n = 6887
p, q = fermat(n)
print('p:', p, 'q:', q, 'p*q:', p*q)
