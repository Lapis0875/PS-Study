# Migrated from ./boj/boj1436.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

number: int = 666
cnt: int = 0
while True:
    s: str = str(number)
    check: int = 0
    for i in range(len(s) - 2):
        if s[i] == "6" and s[i + 1] == "6" and s[i + 2] == "6":
            cnt += 1
            break
    if cnt == N:
        print(number)
        break
    number += 1
