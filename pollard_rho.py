from math import gcd
from random import randrange

from modular_pow import mod_pow
from solovoy_strassen import solovoy_strassen


def check_n(n, prime_check):
    if n in (1, 2):
        raise Exception('n nem osszetett. Pollard rho-modszere paratlan osszetett szamokra alkalmazhato.')
    if n % 2 == 0:
        raise Exception('n nem paratlan. Pollard rho-modszere paratlan osszetett szamokra alkalmazhato.')

    if prime_check and solovoy_strassen(n):
        raise Exception('n nem osszetett. Pollard rho-modszere paratlan osszetett szamokra alkalmazhato.')


def pollard_rho(n, prime_check=True):
    check_n(n, prime_check)
    x = y = randrange(0, 6)
    res = 1

    while res == 1:
        x = (mod_pow(x, 2, n) + 1) % n
        y1 = (mod_pow(y, 2, n) + 1) % n
        y = (mod_pow(y1, 2, n) + 1) % n
        res = gcd(abs(x - y), n)
        if res == n:
            return pollard_rho(n, prime_check)

    return res


if __name__ == "__main__":
    n = 91
    print(n, 'egy faktorja', pollard_rho(n))
