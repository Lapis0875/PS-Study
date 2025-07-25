# Migrated from ./boj/boj2750.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
numbers: list[int] = sorted(int(stdin.readline()) for _ in range(N))
for i in numbers:
    print(i)