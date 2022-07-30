from fractions import Fraction


def iter_squaring(x, y, n):
    res = 1
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res = mod_mul(res, j, n)
        i *= 2
        j = mod_mul(j, j, n)
    return res


def mod_mul(x, y, n):
    res = 0
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res += j
            res %= n
        i *= 2
        j *= 2
        j %= n
    return res


def pnk(n, k):
    return Fraction(2 ** (n - k) * (n - k + 1) + 2 ** (2 * n - k) * (k - 1)) / Fraction((2 ** n - 1) ** 2)


def mnk(n, k):
    x = pnk(n, k)
    return x.numerator * x.denominator


def actual(n, k, m):
    numerator = (mod_mul(iter_squaring(2, n - k, m), n - k + 1, m) + mod_mul(iter_squaring(2, 2 * n - k, m), k-1, m)) % m
    denominator = iter_squaring((iter_squaring(2, n, m) - 1) % m, 2, m)
    return mod_mul(numerator, denominator, m)
