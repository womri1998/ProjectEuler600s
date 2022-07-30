from math import ceil


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


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def p_divisibility(p, n):
    if n == 0:
        return 0
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count


def p_factorial_divisibility(p, n):
    i, count = 1, 0
    while p ** i <= n:
        count += n // p ** i
        i += 1
    return count


def binomial_divisors(n, m, primes):
    exponents = [0] * len(primes)
    for i in range(len(primes)):
        d = p_factorial_divisibility(primes[i], n)
        exponents[i] += d * n
        cur_low, cur_high = 0, d
        for k in range(n):
            exponents[i] -= cur_low + cur_high
            cur_low += p_divisibility(primes[i], k + 1)
            cur_high -= p_divisibility(primes[i], n - k)
    return divisors_sum(exponents, primes, m)


def euclid(n, m):
    if n < m:
        n, m = m, n
    x, y = (n, 1, 0), (m, 0, 1)
    while y[0] != 0:
        k = x[0] // y[0]
        x, y = y, (x[0] % y[0], x[1] - k * y[1], x[2] - k * y[2])
    return x


was = {}


def progression_sum(a1, q, n, m):
    if (a1, q, n) in was:
        return was[(a1, q, n)]
    else:
        res = (a1 * (iter_squaring(q, n, m) - 1) * euclid(q - 1, m)[2]) % m  # euclid gives invers at [2] if n, m are coprime
        was[(a1, q, n)] = res
        return res


def divisors_sum(exponents, primes, m):
    res = 1
    for i in range(len(exponents)):
        res *= progression_sum(1, primes[i], exponents[i] + 1, m)
        res %= m
    return res


def factorization(n, primes):
    factors = [0] * len(primes)
    for i in range(len(primes)):
        while n % primes[i] == 0:
            n //= primes[i]
            factors[i] += 1
    return factors


def add(a, b):  # assuming len(a) >= len(b)
    for i in range(len(b)):
        a[i] += b[i]
    return a


def result(n, m):
    primes = gen_primes(n + 1)
    res, cur, factorial = 0, [0] * len(primes), [0] * len(primes)
    for i in range(1, n + 1):
        print(i, divisors_sum(cur, primes, m), res)
        res += divisors_sum(cur, primes, m)
        fact = factorization(i, primes)
        factorial = add(factorial, fact)
        change = [fact[j] * i - factorial[j] for j in range(len(primes))]
        cur = add(cur, change)
    return (res - 1) % m
