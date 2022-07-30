import numpy as np

class Block:
    n = 0

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def union(self, other):
        if self.end + other.start <= Block.n:
            return Block(self.start, other.end)


def solve(m: int) -> int:
    s = bin(m)[:1:-1]
    current = [(Block(i + 1, j + 1), 1) for i in range(Block.n) for j in range(Block.n)]
    result = [(Block(i + 1, j + 1), 1) for i in range(Block.n) for j in range(Block.n)]
    for i in range(len(s)):
        last = current
        for s1 in range(1, Block.n + 1):
            for e1 in range(1, Block.n + 1):
                for s2 in range(1, Block.n - e1 + 1):
                    for e2 in
        if s[i] == '1':



def main(n, m):
    Block.n = n
    print(solve(m))
