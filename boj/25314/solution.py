# Migrated from ./boj/boj25314.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())
Q = N // 4
print("long " * (Q + 1 if N % 4 else Q) + "int")
