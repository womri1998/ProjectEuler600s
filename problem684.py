from typing import Generator
from modulo import mod


def fib(n: int) -> Generator[tuple[int, int], None, None]:
    a, b = 0, 1
    for i in range(n):
        yield i, a
        a, b = b, a + b


def s(n: int) -> int:
    total = 0
    for i, k in enumerate(range(n - 9, n % 9 - 1, -9)):
        total += (sum(range(10)) + k * 9) * 10 ** i
    total += sum(range(n % 9 + 1)) * 10 ** (i + 1)
    return total


def s2(n: int, m: int = 10 ** 9 + 7, i: int = None) -> int:
    if i:
        print(i, n)
    k = n % 9
    digits = n // 9
    total = (k + 6) * (mod(10, m) ** digits - 1) - 9 * digits
    total += sum(range(n % 9 + 1)) * mod(10, m) ** digits
    result = total.residue
    return result


if __name__ == "__main__":
    print(s(20), s2(20))
    sequence = list(fib(91))[2:]
    print(sum((s2(n, i=i) for i, n in sequence)) % (10 ** 9 + 7))
