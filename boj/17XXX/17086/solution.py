from heapq import heappush, heappop

input = open(0).readline

MAX_DIST = 52
MOVES = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
N, M = map(int, input().split())
grid = [[MAX_DIST] * 50 for _ in range(50)]
sharks = []
queue = []
max_safety_dist = 0

for r in range(N):
    for c, tile in enumerate(map(int, input().split())):
        if tile == 1:
            sharks.append((r, c))
            grid[r][c] = 0

def bfs(r, c):
    queue.clear()
    heappush(queue, (0, r, c))
    
    while queue:
        dist, r, c = heappop(queue)
        
        for dr, dc in MOVES:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and (dist + 1) < grid[nr][nc]:
                grid[nr][nc] = dist + 1
                heappush(queue, (dist + 1, nr, nc))

for r, c in sharks:
    bfs(r, c)

for r in range(N):
    for c in range(M):
        max_safety_dist = max(max_safety_dist, grid[r][c])

print(max_safety_dist)
