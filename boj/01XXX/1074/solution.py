from sys import stdin
from typing import Final

N: Final[int]
R: Final[int]
C: Final[int]
N, R, C = map(int, stdin.readline().split())

def solve(n: int, r: int, c: int) -> int:
    # 종료 조건
    if n == 0:
        return 0
    half: int = 1 << (n - 1)
    
    # 사분면 쪼개기
    if r < half:
        if c < half:
            return solve(n - 1, r, c)
        else: # c >= half
            return half * half + solve(n - 1, r, c - half)
    else:
        if c < half:
            return 2 * half * half + solve(n - 1, r - half, c)
        else:
            return 3 * half * half + solve(n - 1, r - half, c - half)

print(solve(N, R, C))