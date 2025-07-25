# Migrated from ./boj/boj1193.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

i: int = 1
while (N > i):
    N -= i
    i += 1

if i % 2:
    print(f"{i + 1 - N}/{N}")
else:
    print(f"{N}/{i + 1 - N}")