APPROX = 10 ** 30


def p(l: str, n: int) -> int:
    power = 1
    index = 0
    while power > APPROX:
        power //= 10
    while n != 0:
        if index % 10 ** 6 == 0:
            print(index, n)
        index += 1
        power *= 2
        if power > APPROX:
            power //= 10
        if str(power).startswith(l):
            n -= 1
    return index


if __name__ == "__main__":
    print(p('12', 1))
    print(p('12', 2))
    print(p('123', 678910))
