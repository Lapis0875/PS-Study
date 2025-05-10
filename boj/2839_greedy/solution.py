# Migrated from ./boj/boj2839_greedy.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())

count: int = 0

while N >= 0:
    if N % 5 == 0:
        count += N // 5
        N = 0
        break
    else:
        N -= 3
        count += 1
print(count if N == 0 else -1)