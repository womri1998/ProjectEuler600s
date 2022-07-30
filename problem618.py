def fib(n):
    if n == 1:
        return 1
    a, b = 1, 1
    i = 2
    while i < n:
        a, b = a + b, a
        i += 1
    return a
