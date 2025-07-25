from sys import stdin, setrecursionlimit
from typing import Final, Literal, cast

setrecursionlimit(10 ** 6)

type Tile = Literal["R", "G", "B"]
N: Final[int] = int(stdin.readline())
Picture: Final[list[list[Tile]]] = [cast(list[Tile], list(stdin.readline().strip())) for _ in range(N)]

def normal_dfs(y: int, x: int):
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= nx < N and 0 <= ny < N and Picture[ny][nx] == Picture[y][x] and not visited[ny][nx]:
            visited[ny][nx] = True
            normal_dfs(ny, nx)
    
visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
normal_cnt: int = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = True
            normal_dfs(y, x)
            normal_cnt += 1

def colorblind_dfs(y: int, x: int):
    this_color = Picture[y][x]
    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
            next_color = Picture[ny][nx]
            if (next_color == "B" if this_color == "B" else next_color != "B"):
                visited[ny][nx] = True
                colorblind_dfs(ny, nx)

visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
colorblind_cnt: int = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = True
            colorblind_dfs(y, x)
            colorblind_cnt += 1
print(normal_cnt, colorblind_cnt)