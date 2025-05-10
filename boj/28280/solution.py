# Migrated from ./boj/boj28280.py by boj_validator
from sys import stdin
from collections import deque
from typing import Final, Literal

MAX: Final[int] = 4000001
visited: list[bool] = [False] * MAX

def BFS(K: int) -> int | Literal["Wrong proof!"]:
    q: deque[tuple[int, int]] = deque([(1, 0)])     # (number, count)
    while q:
        x, count = q.pop()
        if not visited[x]:
            print(f"({x},{count})")
            visited[x] = True
            if x == K:
                return count
            
            if x > 1:
                q.append((x - 1, count + 1))
            if x <= 2000000:
                q.append((2 * x, count + 1))
    return "Wrong proof!"

T: Final[int] = int(stdin.readline())
for _ in range(T):
    K: int = int(stdin.readline())
    print(BFS(K))
    