from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
arr: list[int] = sorted(int(stdin.readline()) for _ in range(N))


for i in arr:
    print(i)
    