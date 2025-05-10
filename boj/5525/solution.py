# Migrated from ./boj/boj5525.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())
M: int = int(stdin.readline())
S: str = stdin.readline()[:-1]

count: int = 0

for i in range(M):
    if S[i] != "I":
        continue
    repeat: int = 0
    while i < M - 2 and (S[i + 1] == "O" and S[i + 2] == "I"):
        repeat += 1
        if (repeat == N):        # I (OI)xN = P_N
            count += 1
            break
        i += 2

print(count)
