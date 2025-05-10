# Migrated from ./boj/boj21736.py by boj_validator
from collections import deque
from sys import stdin
from typing import cast, Literal

Tile = Literal["O", "X", "I"]
Location = tuple[int, int]
N, M = map(int, stdin.readline().split())
start: Location = (-1, -1)
campus: list[list[Tile]] = []
visited: list[list[bool]] = [[False] * M for _ in range(N)]

for i in range(N):
    line: list[Tile] = []
    line_str: list[Tile] = cast(list[Tile], stdin.readline()[:-1])
    for j, char in enumerate(line_str):
        line.append(char)
        if char == "I":
            start = (j, i)
    campus.append(line)
            
q: deque[tuple[int, int]] = deque([start])
people: int = 0

while q:
    point: Location = q.popleft()
    x, y = point
    # print(f">>> ({x}, {y})", end="")
    
    if not visited[y][x]:
        # print("[ ✅ ]")
        if campus[y][x] == "X":     # 도연이는 아쉽게도 벽을 뚫고 이동할 수는 없다.
            continue
        
        if campus[y][x] == "P":     # 도연이는 친구를 1 (명) 얻었다!
            people += 1
        
        if x >= 1:
            q.append((x - 1, y))
        if x <= M - 2:
            q.append((x + 1, y))
        if y >= 1:
            q.append((x, y - 1))
        if y <= N - 2:
            q.append((x, y + 1))
        
        visited[y][x] = True
    # else:
    #     print("[ ❌ ]")

if people == 0:
    print("TT")
else:
    print(people)