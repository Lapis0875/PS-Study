from sys import stdin
from typing import Final
from sys import maxsize

N: Final[int] = int(stdin.readline())
DP: list[int] = [0, 1]

for i in range(2, N + 1):
    min_v: int = maxsize
    j: int = 1
    while (j_sq := j ** 2) <= i:
        min_v = min(min_v, DP[i - j_sq])
        j += 1
    
    DP.append(min_v + 1)

print(DP[N])
