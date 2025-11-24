input = open(0).readline
INF = 100_000_001
N, M = map(int, input().split())
edges = [None] * (M)
for e in range(M):
    edges[e] = tuple(map(int, input().split()))

distance = [INF] * (N + 1)
def bellman_ford(start):
    distance[start] = 0
    for v in range(N - 1):
        for e in range(M):
            s, e, c = edges[e]
            new_dist = distance[s] + c
            if distance[s] != INF and distance[e] > new_dist:
                distance[e] = new_dist
    
    # 음의 사이클이 있는지 검사
    for e in range(M):
        s, e, c = edges[e]
        new_dist = distance[s] + c
        if distance[s] != INF and distance[e] > new_dist:
            return True
    return False

has_negative_cycle = bellman_ford(1)
if has_negative_cycle:
    print("-1")
else:
    for v in range(2, N + 1):
        print("-1" if distance[v] == INF else distance[v])
