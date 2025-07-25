from heapq import heappop, heappush
input = open(0).readline
print = open(1, "w").write
N = int(input())    # 도시(정점)의 개수
M = int(input())    # 버스(간선)의 개수

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

S, E = map(int, input().split())  # 출발지와 도착지
INF = 100_000_000_001
distance = [INF for _ in range(N + 1)]
distance[S] = 0
pq = []
heappush(pq, (0, S))  # (거리, 정점)
while pq:
    dist, node = heappop(pq)
    if distance[node] < dist:
        continue
    for next_node, weight in edges[node]:
        new_dist = dist + weight
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

print(f"{distance[E]}\n")

