from heapq import heappop, heappush

input = open(0).readline
N, M, X = map(int, input().split())
INF = int(1e9)

# 간선 입력
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    edges[u].append((v, cost)) # 유향 그래프
edges

# Dijkstra
def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))  # (비용, 정점)
    
    while pq:
        cost, u = heappop(pq)
        if distance[u] < cost:  # 이미 더 낮은 비용으로 갈 수 있다면 굳이 반영하지 않는다.
            continue
        for v, c in edges[u]:
            new_dist = cost + c
            if new_dist < distance[v]:
                distance[v] = new_dist
                heappush(pq, (distance[v], v))
    
    return distance

to_X = dijkstra(X)  # X에서 다른 모든 정점까지의 최단 거리

max_distance = 0
for i in range(1, N + 1):
    distance = to_X[i] + dijkstra(i)[X]  # i에서 X까지의 최단 거리
    max_distance = max(max_distance, distance)

# 결과 출력
print(max_distance)  # X에서 다른 모든 정점까지의 최단 거리 중 최대값
