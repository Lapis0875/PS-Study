# Migrated from ./boj/boj1929.py by boj_validator
from sys import stdin

M, N = map(int, stdin.readline().split())

sieve: list[int] = [False, False]
sieve.extend(True for _ in range(2, N + 1))     # 두 정수의 최댓값까지 체를 만들어둔다.

for i in range(2, N + 1):
    if sieve[i]:
        j: int = 2
        while (x := i * j) <= N:
            sieve[x] = False
            j += 1

for i in range(M, N + 1):
    if sieve[i]:
        print(i)
