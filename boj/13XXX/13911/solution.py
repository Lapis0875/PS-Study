from heapq import heappush, heappop
INF = 100_000_001
input = open(0).readline
V, E = map(int, input().split())
graph = tuple([] for _ in range(V + 3))
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

M, x = map(int, input().split())
mcdonalds = tuple(map(int, input().split()))
for m in mcdonalds:
    graph[V + 1].append((m, 0)) # 더미 노드인 V+1번에 맥도날드 정점을 모두 연결해 한 번의 다익스트라로 최단거리 계산 처리

S, y = map(int, input().split())
starbucks = tuple(map(int, input().split()))
for s in starbucks:
    graph[V + 2].append((s, 0)) # 더미 노드인 V+2번에 스타벅스 정점을 모두 연결해 한 번의 다익스트라로 최단거리 계산 처리

queue = []
def dijkstra(src):
    distance = [INF] * (V + 3)
    distance[src] = 0
    queue.clear()
    heappush(queue, (0, src))
    while queue:
        c, u = heappop(queue)
        if c > distance[u]:
            continue

        for v, w in graph[u]:
            if c + w < distance[v]:
                distance[v] = c + w
                heappush(queue, (distance[v], v))
            
    return distance

# 맥도날드와 스타벅스를 같은 더미 노드에 연결할 시, 한 집에서 맥도날드와 스타벅스의 구분 없이 최단 거리가 계산되므로 각각은 다른 더미 노드로 연결해야 한다.
mcdonalds_dist = dijkstra(V + 1) # 더미 노드 통해서 모든 맥도날드로의 최단 거리 계산하기
starbucks_dist = dijkstra(V + 2) # 더미 노드 통해서 모든 스타벅스로의 최단 거리 계산하기

ans_sum = INF
for i in range(1, V + 1):
    if mcdonalds_dist[i] > x or starbucks_dist[i] > y or mcdonalds_dist[i] == 0 or starbucks_dist[i] == 0: # 맥세권 및 스세권인 집만 해당한다.
        continue
    this_sum = mcdonalds_dist[i] + starbucks_dist[i]
    if this_sum < ans_sum:
        ans_sum = this_sum

print(ans_sum if ans_sum < INF else -1)

