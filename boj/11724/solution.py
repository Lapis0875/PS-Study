from sys import stdin
from typing import Final, cast

N: Final[int]
M: Final[int]
N, M = map(int, stdin.readline().split())

vertices: list[int] = list(range(1, N + 1))
edges: list[list[bool]] = [[False for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    edges[u][v] = True
    edges[v][u] = True

visited: list[bool] = [False for _ in range(N + 1)]

def bfs(v: int):
    """너비 우선 탐색을 수행하는 함수

    Args:
        v (int): 탐색을 시작할 정점
    """
    queue: list[int] = [v]
    visited[v] = True

    while queue:
        v = queue.pop(0)
        vertices.remove(v)
        visited[v] = True

        for u, edge in enumerate(edges[v][1:], 1):
            if edge and not visited[u]:
                queue.append(u)
                visited[u] = True

cnt: int = 0
while len(vertices) > 0:
    bfs(vertices[0])
    cnt += 1

print(cnt)