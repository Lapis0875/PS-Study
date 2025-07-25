# Migrated from ./boj/boj10026.py by boj_validator
from sys import stdin, setrecursionlimit
from typing import Iterable, cast, Final, Literal

Pixel = Literal["R", "G", "B"]
setrecursionlimit(10 ** 6)
N: Final[int] = int(stdin.readline())

picture: list[list[Pixel]] = []
visited: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]

def DFS(x: int, y: int) -> bool:
    """깊이 우선 탐색 (DFS) 방식으로 그림을 탐색한다. 3색 모두 구분한다.

    Args:
        x (int): 방문할 픽셀의 x좌표
        y (int): 방문할 픽셀의 y좌표

    Returns:
        bool: 이번 탐색의 결과로 새로운 그룹을 찾았을 경우, True를 반환한다. 그렇지 않은 경우 False를 반환한다.
    """
    v: bool = visited[y][x]
    # print(f"visited: ({x}, {y}) = {v}")
    if not v:
        print(f">>> Now visiting ({x}, {y}) [color = {picture[y][x]}]")
        visited[y][x] = True
        
        if x > 0 and picture[y][x-1] == picture[y][x]:
            print(f">>> ({x}, {y}) -> ({x-1}, {y})")
            DFS(x - 1, y)
        if x < N - 1 and picture[y][x+1] == picture[y][x]:
            print(f">>> ({x}, {y}) -> ({x+1}, {y})")
            DFS(x + 1, y)
        if y > 0 and picture[y-1][x] == picture[y][x]:
            print(f">>> ({x}, {y}) -> ({x}, {y-1})")
            DFS(x, y - 1)
        if y < N - 1 and picture[y+1][x] == picture[y][x]:
            print(f">>> ({x}, {y}) -> ({x}, {y+1})")
            DFS(x, y + 1)

    return v

def DFS_Colorblind(x: int, y: int) -> bool:
    """깊이 우선 탐색 (DFS) 방식으로 문제를 풀이한다. 적록색약을 적용한다.

    Args:
        x (int): 방문할 픽셀의 x좌표
        y (int): 방문할 픽셀의 y좌표

    Returns:
        bool: 이번 탐색의 결과로 새로운 그룹을 찾았을 경우, True를 반환한다. 그렇지 않은 경우 False를 반환한다.
    """
    v: bool = visited[y][x]
    # print(f"visited: ({x}, {y}) = {v}")
    if not v:
        print(f">>> Now visiting ({x}, {y}) [color = {picture[y][x]}]")
        visited[y][x] = True
        color = picture[y][x]
        
        if color == "B":
            if x > 0 and picture[y][x-1] == "B":
                print(f">>> ({x}, {y}) -> ({x-1}, {y})")
                DFS(x - 1, y)
            if x < N - 1 and picture[y][x+1] == "B":
                print(f">>> ({x}, {y}) -> ({x+1}, {y})")
                DFS(x + 1, y)
            if y > 0 and picture[y-1][x] == "B":
                print(f">>> ({x}, {y}) -> ({x}, {y-1})")
                DFS(x, y - 1)
            if y < N - 1 and picture[y+1][x] == "B":
                print(f">>> ({x}, {y}) -> ({x}, {y+1})")
                DFS(x, y + 1)
        else:
            if x > 0 and picture[y][x-1] != "B":
                print(f">>> ({x}, {y}) -> ({x-1}, {y})")
                DFS(x - 1, y)
            if x < N - 1 and picture[y][x+1] != "B":
                print(f">>> ({x}, {y}) -> ({x+1}, {y})")
                DFS(x + 1, y)
            if y > 0 and picture[y-1][x] != "B":
                print(f">>> ({x}, {y}) -> ({x}, {y-1})")
                DFS(x, y - 1)
            if y < N - 1 and picture[y+1][x] != "B":
                print(f">>> ({x}, {y}) -> ({x}, {y+1})")
                DFS(x, y + 1)

    return v

for _ in range(N):
    line: list[Pixel] = []
    for pixel in cast(Iterable[Pixel], stdin.readline()[:-1]):
        line.append(pixel)
    picture.append(line)

normal_count: int = 0
colorblind_count: int = 0

for y in range(N):
    for x in range(N):
        normal_count += DFS(x, y)
        colorblind_count += DFS_Colorblind(x, y)

print(normal_count, colorblind_count)
