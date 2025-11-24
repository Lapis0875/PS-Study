from heapq import heappush, heappop
input = open(0).readline

INF = 20
N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
pq = []
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    pq.clear()
    heappush(pq, (0, start))
    while pq:
        dist, vertex = heappop(pq)
        if dist < distance[vertex]:
            continue

        for v, c in graph[vertex]:
            if dist + c < distance[v]:
                distance[v] = dist + c
                heappush(pq, (dist + c, v))
    
    cnt = 0
    for v in range(1, N + 1):
        if distance[v] <= M:
            cnt += items[v - 1]
    return cnt

max_items = 0
for i in range(1, N + 1):
    max_items = max(max_items, dijkstra(i))
print(max_items)
