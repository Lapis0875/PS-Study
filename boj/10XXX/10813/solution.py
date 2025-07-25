# Migrated from ./boj/boj10813.py by boj_validator
from sys import stdin

N, M = map(int, stdin.readline().split())
baskets: list[int] = list(range(N + 1))


for _ in range(M):
    i, j = map(int, stdin.readline().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]

print(" ".join(map(str, baskets[1:])))
