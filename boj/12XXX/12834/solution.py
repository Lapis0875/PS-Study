from queue import PriorityQueue
input = open(0).readline
N, V, E = map(int, input().split())
KIST, SEA_FOOD = map(int, input().split())
INF = 10101

Homes = list(map(int, input().split()))
Edges = [[INF for _ in range(V + 1)] for _ in range(V + 1)]   # 인접 행렬 초기화. 정점의 값이 1부터 시작하므로 0번은 사용하지 않음.

for _ in range(E):
    u, v, weight = map(int, input().split())
    Edges[u][v] = weight
    Edges[v][u] = weight

def dijkstra(start, distance):
    pq = PriorityQueue()
    pq.put((0, start))
    distance[start] = 0
    while not pq.empty():
        dist, current = pq.get()
        if distance[current] < dist:
            # 현재 우선순위 큐에서 꺼낸 상태는 최신 상태가 아님. 따라서 스킵.
            continue
        for i in range(1, V + 1):
            if distance[current] + Edges[current][i] < distance[i]:
                distance[i] = distance[current] + Edges[current][i]
                pq.put((distance[i], i))

res = 0
d1 = [INF for _ in range(V + 1)]
d2 = [INF for _ in range(V + 1)]
# 무방향 그래프이므로, 다익스트라를 통한 최단거리 탐색 결과는 한 점에서 모든 점까지의 거리와도 같다.
dijkstra(KIST, d1)
dijkstra(SEA_FOOD, d2)
for home in Homes:
    res += d1[home] if d1[home] != INF else -1
    res += d2[home] if d2[home] != INF else -1
print(res)
