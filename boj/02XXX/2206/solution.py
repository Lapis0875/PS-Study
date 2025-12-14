from heapq import heappop, heappush
input = open(0).readline
N, M = map(int, input().split())

INF = N * M + 1 # 도달할 수 없는 경우의 거리 값. N x M 크기의 배열에서 반복 없이 최대로 이동할 때의 거리는 N x M이다.
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[INF, True] for _ in range(M)] for _ in range(N)] # 각 칸의 방문 여부 및 벽을 아직 부술 수 있는 지 기록한다.

pq = [(1, 0, 0, True)] # (이동한 거리, r, c, 벽을 부쉈는지의 여부)로 저장한다. 이동한 거리에는 출발 및 도착지점이 모두 포함되어야 하므로 초기값은 1이다.
visited[0][0] = [1, True] # 출발지점은 항상 벽이 아니므로, 벽을 부수지 않은 상태로 방문 처리한다.

while pq:
    dist, r, c, can_break = heappop(pq)
    if r == N-1 and c == M-1: # 종점에 도달한 경우.
        # 거리 값을 우선순위로 사용했으므로, 항상 최단경로에 해당하는 경우부터 조건문에 도달하게 된다.
        print(dist)
        break

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = r + dr
        nc = c + dc
        # 다음 칸이 미로의 범위 안에 있고 / 아직 방문하지 않았거나, 이전에 방문했던 경우보다 더 짧은 거리로 도달한 경우 / 또는 이전에 벽을 부수고 도달했으나 이번에 벽을 부수지않고 도달했다면
        if 0 <= nr < N and 0 <= nc < M and (dist + 1 < visited[nr][nc][0] or (can_break and not visited[nr][nc][1])):
            if maze[nr][nc] == 1 and can_break: # 벽을 부술 수 있는 상태에서 벽을 만난 경우.
                visited[nr][nc][0] = dist + 1
                visited[nr][nc][1] = False # 이후 경로에서는 더 이상 벽을 부술 수 없다.
                heappush(pq, (dist + 1, nr, nc, False))
            elif maze[nr][nc] == 0: # 벽이 아닌 곳을 만난 경우.
                visited[nr][nc][0] = dist + 1
                visited[nr][nc][1] = can_break # 이후 경로에서 벽을 부술 수 있는지 기록
                heappush(pq, (dist + 1, nr, nc, can_break))
else:
    print(-1)

