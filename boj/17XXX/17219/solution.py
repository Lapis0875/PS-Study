# Migrated from ./boj/boj17219.py by boj_validator
from sys import stdin

N, M = map(int, stdin.readline().split())
PW: dict[str, str] = {}
for _ in range(N):
    site, pw = stdin.readline()[:-1].split()
    PW[site] = pw

for _ in range(M):
    print(PW[stdin.readline()[:-1]])