from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
Stairs: Final[list[int]] = [0] + [int(stdin.readline()) for _ in range(N)]
DP: list[int] = [0 for _ in range(N + 1)]
Path: list[int] = [0 for _ in range(N + 1)]

# 1번 계단은 밟게되면 비교할 이전 계단이 없으므로, 초기값으로써 미리 저장.
DP[1] = Stairs[1]
Path[1] = 0

for i in range(2, N + 1):
    print(Path[i-2:i], i)
    if Path[i-1] - Path[i-2] == 1 and Path[i-1] - Path[i-2] == 1:
        DP[i] = DP[i-2] + Stairs[i]
        Path[i] = i-2
    else:
        DP[i], k = max((DP[i-2] + Stairs[i], i-2), (DP[i-1] + Stairs[i], i-1))
        Path[i] = k

print(DP)
print(Path)
print(DP[N])
