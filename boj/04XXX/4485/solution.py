from heapq import heappush, heappop

input = open(0).readline
tc = 1
tiles = [[0] * 125 for _ in range(125)]
visitied = [[False] * 125 for _ in range(125)]
queue = []
N = 0
DIFF = ((-1, 0), (0, -1), (0, 1), (1, 0))

def bfs():
    queue.clear()
    heappush(queue, (tiles[0][0], 0, 0))
    visitied[0][0] = True
    while queue:
        cost, r, c = heappop(queue)
        if r == N - 1 and c == N - 1:
            return cost
        for dr, dc in DIFF:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and not visitied[nr][nc]:
                visitied[nr][nc] = True
                heappush(queue, (cost + tiles[nr][nc], nr, nc))


while True:
    N = int(input())
    if N == 0:
        break

    for r in range(N):
        for c, v in enumerate(map(int, input().split())):
            tiles[r][c] = v
            visitied[r][c] = False
    
    res = bfs()
    print(f"Problem {tc}: {res}")
    tc += 1
