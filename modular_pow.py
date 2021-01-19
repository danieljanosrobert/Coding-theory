def mod_pow(base, exponent, mod):
    x = 1
    y = base
    while exponent > 0:
        if exponent % 2 == 1:
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod
