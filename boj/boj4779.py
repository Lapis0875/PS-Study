from sys import stdin, setrecursionlimit
from typing import Callable, Literal

setrecursionlimit(10 ** 6)

arr: list[Literal["-", " "]] = []

# 0 ~ 26 => 0 ~ [8] / 9 ~ 17 / [18] ~ 26
# 0 ~ 8 => 0 ~ [2] / [3] ~ 5 / 6 ~ 8
# 18 ~ 26 => 18 ~ 20 / [21] ~ 23 / 24 ~ 26

def cantorian(start: int, end: int):
    if start >= end:
        return
    gap: int = (end - start) // 3
    l: int = start + gap
    r: int = end - gap
    for i in range(l + 1, r):
        arr[i] = " "
    cantorian(start, l)
    cantorian(r, end)

for N in map(int, stdin):
    arr_len: int = 3 ** N
    arr.clear()
    arr.extend("-" for _ in range(arr_len))
    gap_size: int = arr_len // 3
    cantorian(0, arr_len - 1)
    print("".join(arr))
