from math import factorial


def nck(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def add(v, u):
    w = []
    if len(v) < len(u):
        v, u = u, v
    i = 0
    while i < len(u):
        w.append(u[i] + v[i])
        i += 1
    while i < len(v):
        w.append(v[i])
        i += 1
    return w


def multiply(v, u):
    if len(v) == 0 or len(u) == 0:
        return []
    w = [0] * (len(v) + len(u) - 1)
    for i in range(len(v)):
        for j in range(len(u)):
            w[i + j] += v[i] * u[j]
    return w


def power(v, n):
    w = [1]
    for i in range(n):
        w = multiply(w, v)
    return w


hit_chance = [1]


def miss(n):
    v = [0]
    for i in range(n):
        v = add(v, multiply([nck(n, i), -1 * nck(n, i)], power([-2, 1], n - i - 1)))
    return v
