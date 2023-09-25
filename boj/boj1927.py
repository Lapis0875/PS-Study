from sys import stdin
from queue import PriorityQueue
from typing import Final

N: Final[int] = int(stdin.readline())
pq: PriorityQueue[int] = PriorityQueue()


for _ in range(N):
    n: int = int(stdin.readline())
    
    if n == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get())
    else:
        pq.put(n)
