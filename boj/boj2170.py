from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
lines: list[tuple[int, int]] = sorted(tuple(map(int, stdin.readline().split())) for _ in range(N))

start = -1000000001
end = -1000000001
length: int = 0

for l, r in lines:
    if l > end:
        length += (end - start)
        start = l
    if r > end:
        end = r

length += (end - start)

print(length)