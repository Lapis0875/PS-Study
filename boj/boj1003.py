from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())

fiboarr: list[int] = [0, 1]
fiboarr.extend([0] * 39)

def fibo(n: int) -> int:
    if n == 0 or n == 1:
        return fiboarr[n]
    elif fiboarr[n] == 0:
        fiboarr[n] = fibo(n - 1) + fibo(n - 2)
    return fiboarr[n]

for _ in range(T):
    N: Final[int] = int(stdin.readline())
    if N == 0:
        print(1, 0)
    else:
        print(fibo(N - 1), fibo(N))
