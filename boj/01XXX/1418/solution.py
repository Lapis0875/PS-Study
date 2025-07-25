# Migrated from ./boj/boj1418.py by boj_validator
from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

cnt: int = 0
for i in range(1, N + 1):
    # print(f"{i} => ", end="")
    for j in range(2, K + 1):
        while i % j == 0:
            i //= j
    print(i)
    if i == 1:
        cnt += 1

print(cnt)
