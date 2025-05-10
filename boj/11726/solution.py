# Migrated from ./boj/boj11726.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

memo: list[int] = [0, 1, 2]     # 2x1 = 1가지, 2x2 는 2가지 (= 또는 ||)

if N > 2:
    """
    2 x 3:
    [ |||, |=, =| ] => 3가지. 자세히 보면, memo[n-1] + memo[n-2]
    
    2 x 4:
    [ ||||, ||=, |=|, =||, == ]=> 5가지. 자세히 보면,
    """
    for _ in range(3, N + 1):
        memo.append(memo[-1] + memo[-2])
print(memo[N] % 10007)
