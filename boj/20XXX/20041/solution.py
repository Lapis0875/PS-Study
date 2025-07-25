from sys import stdin
from typing import Final, cast

Coordinate = tuple[int, int]
INF: Final[int] = 10 ** 9 + 1
N: Final[int] = int(stdin.readline())
cops: list[Coordinate] = [cast(Coordinate, tuple(map(int, stdin.readline().split()))) for _ in range(N)]
thief: Coordinate = cast(Coordinate, tuple(map(int, stdin.readline().split())))

flags: list[bool] = [False, False, False, False]

for cop in cops:
    x, y = cop
    rel_x = x - thief[0]
    rel_y = y - thief[1]
    if abs(rel_x + INF) + abs(rel_y) <= INF:                    # (INF, 0) 에 도달하는게 경찰이 더 빠른 경우
        flags[0] = True
    if abs(rel_y - INF) + abs(rel_y) <= INF:      # (-INF, 0) 에 도달하는게 경찰이 더 빠른 경우
        flags[1] = True
    if abs(rel_x) + abs(rel_y + INF) <= INF:      # (0, INF) 에 도달하는게 경찰이 더 빠른 경우
        flags[2] = True
    if abs(rel_x) + abs(rel_y - INF) <= INF:      # (0, -INF) 에 도달하는게 경찰이 더 빠른 경우
        flags[3] = True

if all(flags):
    print("NO")
else:
    print("YES")
