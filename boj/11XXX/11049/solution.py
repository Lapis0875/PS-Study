from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
d: Final[list[int]] = [0 for _ in range(N + 1)]

d[0:2] = map(int, stdin.readline().split())
for i in range(2, N + 1):
    _, c = stdin.readline().split()
    d[i] = int(c)

M: list[list[int]] = [[0] * (N + 1) for _ in range(N + 1)]

for diagonal in range(1, N):
    for i in range(1, N - diagonal + 1):
        j: int = i + diagonal
        M[i][j] = min(M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j] for k in range(i, j))

print(M[1][N])
