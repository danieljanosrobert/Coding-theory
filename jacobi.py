"""
P = p1*p2*p3*pk
(1 / P) = 1
(a / PQ) = (a / P)(a / Q)
(ab / P) = (a / P)(b / P)
(-1 / Q) = (-1)^((Q - 1) / 2)
(2 / Q) = (-1)^((Q^2 - 1) / 8)
(P / Q)(Q / P) = (-1)^(((P - 1) / 2) * ((Q - 1) / 2))
a % P = b == (a / P) = (b / P)
"""
from random import randrange

from sympy import jacobi_symbol


def check_p(p):
    if p < 0:
        raise Exception('p nem pozitiv. Jacobi szimbolum szamitasahoz p paratlan kell legyen (es nem 1).')
    if p == 2:
        raise Exception('p prim, de nem paratlan. Jacobi szimbolum szamitasahoz p paratlan kell legyen (es nem 1).')
    if p % 2 == 0:
        raise Exception('p nem paratlan. Jacobi szimbolum szamitasahoz p paratlan kell legyen (es nem 1).')


def jacobi(a, p):
    check_p(p)
    if a >= p or a < 0:
        return int(jacobi(a % p, p))
    if a == 0 or a == 1:
        return a
    elif a == 2:
        return 1 if p % 8 in (1, 7) else -1
    elif a == p - 1:
        return 1 if p % 4 == 1 else -1
    if a % 2 == 0:
        return jacobi(a/2, p) if p % 8 in (1, 7) else -1 * jacobi(a/2, p)
    else:
        if p % 4 == 1 or a % 4 == 1:
            return jacobi(p, a)
        else:
            return -1 * jacobi(p, a)


if __name__ == "__main__":
    N = 1000
    for _ in range(100):
        a = randrange(1, N)
        n = randrange(a + 1, 2 * N)
        if n % 2 == 0:
            n += 1

        j1 = jacobi_symbol(a, n)
        j2 = jacobi(a, n)
        print('\033[91m' if j1 != j2 else '\033[92m', 'a: ', a, '\tp: ', n, '\tjacobi: ',
              j1, '\teredmeny: ', j2)
