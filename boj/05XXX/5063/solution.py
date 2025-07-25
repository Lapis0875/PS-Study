# Migrated from ./boj/boj5063.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

for _ in range(N):
    r, e, c = map(int, stdin.readline().split())
    res = e - c - r
    if res > 0:
        print("advertise")
    elif res < 0:
        print("do not advertise")
    else:
        print("does not matter")