# Migrated from ./boj/boj2178.py by boj_validator
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

maze: list[list[bool]] = []

# Step 1. Build Maze!
for _ in range(N):
    line: str = stdin.readline()[:-1]
    row: list[bool] = []
    for tile in line:   # length = M
        row.append(tile == "1")
    maze.append(row)

# Step 2. BFS!
q: deque[tuple[int, int]] = deque([(0, 0)])
while q:
    x, y = q.popleft()
    
