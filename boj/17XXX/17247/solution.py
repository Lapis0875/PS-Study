from sys import stdin
from typing import Final

def taxi_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    """두 좌표 사이의 택시 거리를 계산한다.

    Args:
        x1 (int): 첫 번째 위치의 x좌표
        y1 (int): 첫 번째 위치의 y좌표
        x2 (int): 두 번째 위치의 x좌표
        y2 (int): 두 번째 위치의 y좌표

    Returns:
        int: 두 좌표 사이의 택시 거리
    """
    return abs(x2 - x1) + abs(y2 - y1)

N, M = map(int, stdin.readline().split())   # N: 높이, M: 너비
MAP: tuple[list[int], ...] = tuple([] for _ in range(N))
Coords: list[tuple[int, int]] = []
for y in range(N):
    for x, v in enumerate(map(int, stdin.readline().split())):
        MAP[y].append(v)
        if v == 1:
            Coords.append((x, y))

print(taxi_dist(Coords[0][0], Coords[0][1], Coords[1][0], Coords[1][1]))
