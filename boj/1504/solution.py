from heapq import heappush, heappop
INF = 200_000_000
input = open(0).readline
N, E = map(int, input().split())
edges = [[] for _ in range(N + 1)]

if E == 0:
    print(-1)
    exit()

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

def dijkstra(start):
    INF = 100_000_000_001             # 방문 불가능한 정점의 거리를 나타낼 상수
    distance = [INF for _ in range(N + 1)] # 출발 정점 S로부터 각 정점 사이의 최단거리를 저장할 배열
    distance[start] = 0                   # S에서 S까지의 거리는 0이다.

    pq = []                           # 우선순위 큐로 사용할 배열 선언
    heappush(pq, (0, start))              # (거리, 정점)
    while pq:
        dist, node = heappop(pq)      # 우선순위 큐에서 원소 꺼내오기
        if distance[node] < dist: 
            continue
        for next_node, weight in edges[node]: # 다음 노드를 순회하며 우선순위 큐에 넣기
            new_dist = dist + weight
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(pq, (new_dist, next_node))
    return distance

A, B = map(int, input().split())
dist_start = dijkstra(1)
dist_A = dijkstra(A)
dist_end = dijkstra(N)

dist = min(dist_start[A] + dist_A[B] + dist_end[B], dist_start[B] + dist_A[B] + dist_end[A])
print(-1 if dist >= INF else dist)