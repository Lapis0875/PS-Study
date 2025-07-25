from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

cnt: int = N
i: int = 2
while i < N:
    q = (N - 1) // i
    j: int = (N - 1) // q
    cnt += (1 + q) * (j - i + 1)
    i = j + 1
if N != 1:
    cnt += 1

print(cnt)
