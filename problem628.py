def goods(n, m):
    total = n - 2
    fact = 1
    for i in range(1, n):
        if i % 10 ** 6 == 0:
            print(i)
        fact *= i
        fact %= m
        total += (n - 3 - i) * fact
        total %= m
    total += fact * n
    return total % m
