from random import randrange

from jacobi import jacobi


def modulo(base, exponent, mod):
    x = 1
    y = base
    while exponent > 0:
        if exponent % 2 == 1:
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod


def solovoy_strassen(p, k = 5):
    if p < 2:
        return False
    if p % 2 == 0:
        return True if p == 2 else False

    for i in range(k):

        a = randrange(p - 1) + 1
        jacobian = (p + jacobi(a, p)) % p
        mod = modulo(a, (p - 1) / 2, p)

        if jacobian == 0 or mod != jacobian:
            return False

    return True


#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def primes(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


if __name__ == "__main__":
    FROM = 21310421
    TO = 21310721
    cnt = 0

    for i in range(FROM, TO):
        prime_found = solovoy_strassen(i)
        if prime_found:
            cnt += 1
        print('\033[94m' if prime_found else '\033[90m', i, end=' ')

    list_of_primes = [x for x in primes(TO) if x > FROM]
    print('\033[91m' if cnt != len(list_of_primes) else '\033[92m', '\nprimek ', FROM, 'es', TO, 'kozt:',
          len(list_of_primes), '- Megtalalt primek a solovoy-strassen algoritmussal:', cnt)
