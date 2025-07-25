from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

pattern: list[str] = ["*", ""]
for idx in range(1, N):
    pattern[idx % 2] += " *"

for row in range(N):
    for line in pattern:
        print(line)