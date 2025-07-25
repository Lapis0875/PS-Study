from math import ceil, floor
from sys import stdin
from typing import Final

A: Final[int]
B: Final[int]
C: Final[int]
A, B, C = map(int, stdin.readline().split())

memo: dict[int, int] = {}

def square_mod(x: int, times: int) -> int:
    if memo[times] != 0:
        return memo[times]
    
    if times > 2:
        res: int = square_mod(x, ceil(times / 2)) % C * square_mod(x, floor(times / 2)) % C
    else:
        res: int = x ** times % C
    
    memo[times] = res
    return res

print(square_mod(A, B))