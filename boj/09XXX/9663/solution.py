from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

cols: list[int] = [0 for _ in range(N + 1)]

def promising(i: int) -> bool:
    for k in range(1, i):
        if cols[i] == cols[k] or abs(cols[i] - cols[k]) == i - k:   # 같은 열에 있거나 / 대각선에 있는 경우
            return False
    return True

cnt: int = 0

def queens(i: int):
    global cnt
    if promising(i):
        if i == N:
            cnt += 1
        else:
            for j in range(1, N + 1):
                cols[i+1] = j
                queens(i + 1)

queens(0)
print(cnt)