from sys import stdin
from math import comb
from typing import Final

T: Final[int] = int(stdin.readline())
for _ in range(T):
    N, M = map(int, stdin.readline().split())
    print(comb(M, N))
