# Migrated from ./boj/boj1931.py by boj_validator
from sys import stdin
from typing import Final, TypeVar
from queue import PriorityQueue

Meeting = tuple[int, int]
N: Final[int] = int(stdin.readline())
pq: PriorityQueue[tuple[int, Meeting]] = PriorityQueue(maxsize=N)

for _ in range(N):
    start, end = map(int, stdin.readline().split())
    pq.put((end, (start, end)))

next_available: int = 0
cnt: int = 0
while not pq.empty():
    _, (start, end) = pq.get()
    if start < next_available:
        continue
    next_available = end
    cnt += 1

print(cnt)