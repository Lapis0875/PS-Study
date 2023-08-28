from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
table: list[int] = [0 for _ in range(N + 1)]
table[3] = table[5] = 1

for i in range(6, N + 1):
    if (table[i-3]):
        table[i] = table[i-3] + 1
    if (table[i-5]):
        table[i] = min(table[i-5] + 1, table[i]) if table[i] else table[i-5] + 1

print(table[N] or -1)