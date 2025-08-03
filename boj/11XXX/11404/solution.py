input = open(0).readline
N = int(input())
M = int(input())
INF = int(1e9)

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    if cost < graph[u][v]:
        graph[u][v] = cost

dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            dist[i][j] = 0
        elif graph[i][j] != INF:
            dist[i][j] = graph[i][j]

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for r in range(1, N + 1):
    print(" ".join(map(lambda d: "0" if d == INF else str(d), dist[r][1:])))