def max_p(p, n):
    i = 0
    while p ** i <= n:
        i += 1
    return p ** (i - 1)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def jump(s):
    j = 1
    for p in primes:
        j *= max_p(p, s)
    return j


def p(s, n):
    j1, j2 = jump(s), jump(s + 1)
    return (n - 1) // j1 - (n - 1) // j2


def result():
    res = 0
    for i in range(1, 32):
        res += p(i, 4 ** i)
        print(i, p(i, 4 ** i), res)
    return res - 1 # off by one, that why -1
