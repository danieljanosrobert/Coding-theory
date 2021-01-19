"""
(1 / p) = 1
(ab / p) = (a / p)(b / p)
(-1 / p) = (-1)^((p - 1) / 2)
(2 / p) = (-1)^((p^2 - 1) / 8)
(p / q)(q / p) = (-1)^(((p - 1) / 2) * ((q - 1) / 2))
a % p = b == (a / p) = (b / p)
"""
from random import randrange

from sympy import legendre_symbol
from prime_generator import primes


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def check_p(p):
    if p < 0:
        raise Exception('p nem pozitiv. Legendre szimbolum szamitasahoz p paratlan prim kell legyen.')
    if p == 2:
        raise Exception('p prim, de nem paratlan. Legendre szimbolum szamitasahoz p paratlan prim kell legyen.')
    if not is_prime(p):
        raise Exception('p nem prim. Legendre szimbolum szamitasahoz p paratlan prim kell legyen.')


def factorize(n):
    result = []

    p = 2
    while True:
        while n % p == 0 and n > 0:
            result.append(int(p))
            n /= p
        p += 1
        if p > n / p:
            break
    if n > 1:
        result.append(int(n))
    return result


def legendre(a, p):
    check_p(p)
    if a >= p or a < 0:
        return legendre(a % p, p)
    if a == 0 or a == 1:
        return a
    elif a == 2:
        return 1 if p % 8 in (1, 7) else -1
    elif a == p - 1:
        return 1 if p % 4 == 1 else -1
    if not is_prime(a):
        prod = 1
        for factor in factorize(a):
            prod *= legendre(factor, p)
            if prod == 0:
                return 0
        return prod
    else:
        if p % 4 == 1 or a % 4 == 1:
            return legendre(p, a)
        else:
            return -1 * legendre(p, a)


if __name__ == "__main__":
    N = 1000
    primes = primes(1000000)
    try:
        for _ in range(100):
            a = randrange(1, 2 * N)

            j1 = legendre_symbol(a, primes[a % len(primes)])
            j2 = legendre(a, primes[a % len(primes)])
            print('\033[91m' if j1 != j2 else '\033[92m', 'a: ', a, '\tp: ', primes[a % len(primes)], '\tlegendre: ',
                  j1, '\teredmeny: ', j2)
    except Exception:
        print('')
