# Migrated from ./boj/boj9610.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
record: list[int] = [0, 0, 0, 0, 0]

for _ in range(N):
    x, y = map(int, stdin.readline().split())
    if x == 0 or y == 0:
        record[4] += 1      # AXIS
    if x > 0:
        if y > 0:
            record[0] += 1  # Q1
        elif y < 0:
            record[3] += 1  # Q4
    elif x < 0:
        if y > 0:
            record[1] += 1  # Q2
        elif y < 0:
            record[2] += 1  # Q3

print(f"Q1: {record[0]}")
print(f"Q2: {record[1]}")
print(f"Q3: {record[2]}")
print(f"Q4: {record[3]}")
print(f"AXIS: {record[4]}")