from sys import stdin
from typing import Final

A: Final[int]
B: Final[int]
A, B = map(int, stdin.readline().split())

M: Final[int] = 1_000_000_007

def modpow(a: int, b: int, m: int) -> int:
    """[ exponenate by squaring ] 거듭제곱을 빠르게 진행하는 알고리즘.

    Args:
        a (int): 밑
        b (int): 지수
        m (int): 모듈로 연산을 수행할 M

    Returns:
        int: a ^ b % m의 결과값
    """
    ret = 1
    while b != 0:
        if b & 1 != 0:
            ret = ret * a % m
        a = a * a % m
        b >>= 1
    return ret

if A == 1:
    print(B % M)
else:
    print( ( ( modpow(A, B, M) - 1 ) % M * pow(A - 1, -1, M) ) % M)
