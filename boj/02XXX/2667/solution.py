from sys import stdin
from typing import Final, Generator, Literal, cast

type Tile = Literal[0, 1]
N: Final[int] = int(stdin.readline())
Map: Final[list[list[Tile]]] = [[] for _ in range(N)]

for row in Map:
    for tile in cast(Generator[Tile, None, None], map(int, stdin.readline().strip())):
        row.append(tile)

visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]

def dfs(y: int, x: int) -> int:
    cnt: int = 1
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= nx < N and 0 <= ny < N and Map[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            cnt += dfs(ny, nx)
    return cnt

res: list[int] = []
for y in range(N):
    for x in range(N):
        if Map[y][x] == 1 and not visited[y][x]:
            visited[y][x] = True
            res.append(dfs(y, x))

print(len(res))
for i in sorted(res):
    print(i)