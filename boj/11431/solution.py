from sys import stdin
from math import ceil
from typing import Final

K: Final[int] = int(stdin.readline().strip())

for idx in range(1, K+1):
    N, S, P = map(int, stdin.readline().split())
    points: list[tuple[int, int]] = [tuple(map(int, stdin.readline().split()))] # (x, y)# 1st point
    total_length: int = 0
    for i in range(N):      # index referencing past point.
        x, y = map(int, stdin.readline().split())
        points.append((x, y))
        if x == points[i][0]:     # vertical
            total_length += abs(y - points[i][1])
        else:
            total_length += abs(x - points[i][0])
    print(f"---\nDebug:\n * total_length: {total_length}")
    print(f"Data Set {idx}:\n{ceil(total_length * S / P)}\n")