input = open(0).readline
INF = 1_000_000_001

N, M, S, T = map(int, input().split())
graph = [[0 if i == j else INF for i in range(301)] for j in range(301)]   # 방향 그래프

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

# 플로이드-워셜
for mid in range(1, N + 1):
    for i in range(1, N + 1):
        if i == mid:
            continue

        for j in range(1, N + 1):
            if j == mid: 
                continue

            new_dist = graph[i][mid] + graph[mid][j]
            if new_dist < graph[i][j]:
                graph[i][j] = new_dist

for i in range(int(input())):
    a1, b1, c1, a2, b2, c2 = map(int, input().split())
    
    # 가능한 4가지 경우 고려하기
    reduced_dist = min(graph[S][T], graph[S][a1] + c1 + graph[b1][T])                          # 1. 도로 1 이용 시 거리
    reduced_dist = min(reduced_dist, graph[S][a2] + c2 + graph[b2][T])                        # 2. 도로 2 이용 시 거리
    reduced_dist = min(reduced_dist, graph[S][a1] + c1 + graph[b1][a2] + c2 + graph[b2][T])    # 3. 도로 1 -> 도로 2 이용 시 거리
    reduced_dist = min(reduced_dist, graph[S][a2] + c2 + graph[b2][a1] + c1 + graph[b1][T])    # 4. 도로 2 -> 도로 1 이용 시 거리
    print(reduced_dist if reduced_dist < INF else -1)
