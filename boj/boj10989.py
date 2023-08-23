from sys import stdin
from typing import Final


N: Final[int] = int(stdin.readline())
count: list[int] = []
for _ in range(N):
    i = int(stdin.readline())
    if (l := len(count)) <= i:
        count.extend([0 for _ in range(i - l + 1)])
    count[i] += 1

for i, c in enumerate(count):
    for _ in range(c):
        print(i)