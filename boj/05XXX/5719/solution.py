from heapq import heappop, heappush
input = open(0).readline

DIST_MAX = float("inf")
edges = [{} for _ in range(500)]
distance = [DIST_MAX] * 500
path = [[] for _ in range(500)]
check = [[False] * 500 for _ in range(500)]

def dijkstra(start):
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        cost, u = heappop(pq)
        if distance[u] < cost:
            continue
        for v in edges[u]:
            new_dist = cost + edges[u][v]
            if new_dist < distance[v]:
                distance[v] = new_dist
                path[v].clear()
                path[v].append(u)
                heappush(pq, (new_dist, v))
            elif new_dist == distance[v]:
                path[v].append(u)

def dfs(v):
    if v == S:
        return

    for u in path[v]:
        if not check[u][v]:
            try:
                del edges[u][v]
            except KeyError:
                pass
            check[u][v] = True
            dfs(u)

while True:
    N, M = map(int, input().split())
    if N == 0: # Test case ends.
        break
    S, D = map(int, input().split())

    # reset variables
    for i in range(N):
        for j in range(N):
            check[i][j] = False
        distance[i] = DIST_MAX
        path[i].clear()
        edges[i].clear()
    
    for _ in range(M):
        u, v, p = map(int, input().split())
        edges[u][v] = p
    
    # First dijkstra to find the shortest path
    dijkstra(S)
    
    # Remove the shortest path edges
    dfs(D)

    # Second dijkstra to find the almost shortest path
    for i in range(N):
        distance[i] = DIST_MAX
    dijkstra(S)

    print(distance[D] if distance[D] < DIST_MAX else -1)
