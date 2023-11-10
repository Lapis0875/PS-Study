from sys import stdin
from typing import Final

N: Final[int]
K: Final[int]
MAX: Final[int] = 100_000
N, K = map(int, stdin.readline().split())

COST: list[int] = [0 for _ in range(MAX + 1)]

def bfs(x: int):
    queue: list[int] = [x]
    
    while queue:
        v: int = queue.pop(0)
        
        if v == K:
            print(COST[v])
            break
        
        # Prepare next iteration.
        for i in (v - 1, v + 1, v * 2):
            if 0 <= i <= MAX and not COST[i]:
                COST[i] = COST[v] + 1
                queue.append(i)

bfs(N)