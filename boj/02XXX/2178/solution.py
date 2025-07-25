from sys import stdin
from typing import Final, Literal

type Tile = Literal[0, 1]
type Pos = tuple[int, int]  # (y, x)
N: Final[int]
M: Final[int]
N, M = map(int, stdin.readline().split())

maze: list[list[Tile]] = [[1 if c == "1" else 0 for c in stdin.readline().strip()] for _ in range(N)]
record: list[list[int]] = [[0 for _ in range(M)] for _ in range(N)]
record[0][0] = 1
queue: list[Pos] = [(0, 0)]
while queue:
    pos: Pos = queue.pop(0)
    # print(pos)
    cy, cx = pos
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        y = cy + dy
        x = cx + dx
        if 0 <= x < M and 0 <= y < N and maze[y][x] == 1 and record[y][x] == 0:
            queue.append((y, x))
            record[y][x] = record[cy][cx] + 1
print(record[N - 1][M - 1])