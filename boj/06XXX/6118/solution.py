from heapq import heappush, heappop
input = open(0).readline
N, M = map(int, input().split())
INF = 50_001
distance = [INF for _ in range(N + 1)]
edges = [[] for _ in range(N + 1)]
queue = []

for _ in range(M):
    A, B = map(int, input().split())
    # 양방향으로 연결됨
    edges[A].append(B)
    edges[B].append(A)

# BFS (우선순위 큐)
heappush(queue, (0, 1))
distance[1] = 0
while queue:
    dist, u = heappop(queue)

    for v in edges[u]:
        if dist + 1 < distance[v]:
            distance[v] = dist + 1
            heappush(queue, (dist + 1, v))

max_dist = 0
min_idx = 0
cnt = 0
for i in range(2, N + 1):
    if distance[i] > max_dist:
        max_dist = distance[i]
        min_idx = i
        cnt = 1
    elif distance[i] == max_dist:
        cnt += 1

print(min_idx, max_dist, cnt)
