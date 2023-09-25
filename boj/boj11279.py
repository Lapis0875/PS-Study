from sys import stdin
from queue import PriorityQueue
from typing import Final

N: Final[int] = int(stdin.readline())
pq: PriorityQueue[tuple[int, int]] = PriorityQueue()
MAX_INT: int = 2 ** 31

for _ in range(N):
    n: int = int(stdin.readline())
    
    if n == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((MAX_INT - n, n))
