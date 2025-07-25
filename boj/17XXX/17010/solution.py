from sys import stdin
from typing import Final

L: Final[int] = int(stdin.readline())

lines: list[str] = []

for _ in range(L):
    count, char = stdin.readline().split()
    lines.append(char * int(count))
for line in lines:
    print(line)