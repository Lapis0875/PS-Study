from sys import stdin
from typing import Final

memo: list[int] = [0, 1, 2, 4]
"""
1 = (1) : 1
2 = (1, 1), (2) : 2
3 = (1, 1, 1), (1, 2), (2, 1), (3) : 4
4 = DP[4 - 1] + DP[4 - 2] + DP[4 - 1] : 7
# [n - 1]을 만드는 경우에서 1을 더하면 n이고, [n - 2]를 만드는 경우에서 2를 더하면 n이며, [n - 3]을 만드는 경우에서 3을 더하면 n이다.
따라서, DP[n] = DP[n - 1] + DP[n - 2] + DP[n - 3]의 점화식을 가진다는 것을 알 수 있다.
"""

T: Final[int] = int(stdin.readline())

last_memo: int = 3

for _ in range(T):
    N: int = int(stdin.readline())
    
    if last_memo < N:
        memo.extend([0] * (N - last_memo))
    
    
        for i in range(last_memo + 1, N + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    print(memo[N])
