from operator import ne
from sys import stdin
from typing import Final

type Map = list[list[int]]
type Coordinate = tuple[int, int]
N: Final[int]   # 행 크기
M: Final[int]   # 열 크기
N, M = map(int, stdin.readline().split())
world: Map = []
res: Map = []
start: Coordinate = (0, 0)      # y, x
for i in range(N):
    row: list[int] = []
    data: list[int] = []
    for j, c in enumerate(map(int, stdin.readline().split())):
        if c == 2:
            start = (i, j)      # y, x
        row.append(c)
        data.append(-1 if c == 1 else 0)
    world.append(row)
    res.append(data)

queue: list[Coordinate] = [start]

while queue:
    y, x = queue.pop(0)
    for i, j in ((1, 0), (0, -1), (-1, 0), (0, 1)):
        new_y = y + i
        new_x = x + j
        if 0 <= new_y < N and 0 <= new_x < M and res[new_y][new_x] == -1:
            if world[new_y][new_x] == 1:
                res[new_y][new_x] = res[y][x] + 1
                queue.append((new_y, new_x))
            elif world[new_y][new_x] == 0:
                res[new_y][new_x] = 0

for row in res:
    print(" ".join(map(str, row)))
