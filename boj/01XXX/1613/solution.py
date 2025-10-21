input = open(0).readline
N, K = map(int, input().split())
INF = 500000

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(K):
    s, e = map(int, input().split())
    graph[s][e] = 1

for mid in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][mid] + graph[mid][j] < graph[i][j]:
                graph[i][j] = graph[i][mid] + graph[mid][j]

for _ in range(int(input())):
    s, e = map(int, input().split())
    if graph[s][e] < INF:
        print("-1")
    elif graph[e][s] < INF:
        print("1")
    else:
        print("0")
