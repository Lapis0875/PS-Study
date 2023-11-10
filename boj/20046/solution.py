from sys import stdin, maxsize
from typing import Final
import heapq

Coordinate = tuple[int, int]
INF: Final[int] = maxsize
m, n = map(int, stdin.readline().split())
graph: list[list[int]] = [list(map(int, stdin.readline().split())) for _ in range(m)]
dx: tuple[int, int, int, int] = (-1, 1, 0, 0)
dy: tuple[int, int, int, int] = (0, 0, -1, 1)

pq: list[tuple[Coordinate, int]] = []
heapq.heapify(pq)
distance: list[list[int]] = [[INF for _ in range(n)] for _ in range(m)]

heapq.heappush(pq, ((0, 0), graph[0][0]))
distance[0][0] = graph[0][0]

if graph[0][0] == -1:
    print(-1)
    exit(0)


while len(pq) > 0:
    (cur_x, cur_y), cur_cost = heapq.heappop(pq)
    
    for x, y in zip(dx, dy):
        nx = cur_x + x
        ny = cur_y + y
        if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] != -1:
            nc: int = cur_cost + graph[ny][nx]
            if nc < distance[ny][nx]:
                distance[ny][nx] = nc
                heapq.heappush(pq, ((nx, ny), nc))

if distance[m-1][n-1] == INF:
    print(-1)
else:
    print(distance[m-1][n-1])