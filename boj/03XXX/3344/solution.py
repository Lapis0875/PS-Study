from sys import stdin, setrecursionlimit
from typing import Final

setrecursionlimit(10**6)

N: Final[int] = int(stdin.readline())

cols: list[int] = [0 for _ in range(N + 1)]

def promising(i: int) -> bool:
    for k in range(1, i):
        if cols[i] == cols[k] or abs(cols[i] - cols[k]) == i - k:   # 같은 열에 있거나 / 대각선에 있는 경우
            return False
    return True

def queens(i: int):
    if promising(i):
        if i == N:
            for i in cols:
                print(i)
            exit(0)
        else:
            for j in range(1, N + 1):
                cols[i+1] = j
                queens(i + 1)

queens(0)