# Migrated from ./boj/boj10816.py by boj_validator
from sys import stdin
from typing import Final, Generator

N: Final[int] = int(stdin.readline())
countMap: dict[int, int] = {}
for i in map(int, stdin.readline().split()):
    try:
        countMap[i] += 1
    except KeyError:
        countMap[i] = 1

M: Final[int] = int(stdin.readline())
print(" ".join(map(lambda n: str(countMap.get(n, 0)), map(int, stdin.readline().split()))))