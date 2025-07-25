# Migrated from ./boj/boj1874.py by boj_validator
from sys import stdin
from typing import Literal

N = int(stdin.readline())
numbers: list[int] = [int(stdin.readline()) for _ in range(N)]

stk: list[int] = []
result: list[Literal["+", "-"]] = []
idx: int = 0

for i in range(1, N + 1):
    stk.append(i)       # push
    result.append("+")

    while stk and stk[-1] == numbers[idx]:
        idx += 1
        stk.pop()
        result.append("-")

if stk:
    print("NO")
else:
    for res in result:
        print(res)
