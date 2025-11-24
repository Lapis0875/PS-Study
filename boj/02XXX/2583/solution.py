from collections import deque
input = open(0).readline

is_blank = [[True] * 100 for _ in range(100)]
visited = [[False] * 100 for _ in range(100)]
queue = deque()

def fill_board(x1, y1, x2, y2):
    for r in range(x1, x2): # [x1,x2)
        for c in range(y1, y2): # [y1,y2)
            is_blank[r][c] = False

M, N, K = map(int, input().split())
DIFF = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(r, c):
    queue.clear()
    queue.append((r, c))
    visited[r][c] = True
    block_size = 1
    while queue:
        r, c = queue.popleft()

        for dr, dc in DIFF:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and is_blank[nr][nc]:
                visited[nr][nc] = True
                block_size += 1
                queue.append((nr, nc))
    return block_size

for i in range(K):
    fill_board(*map(int, input().split())) # (x1, y1, x2, y2)

cnt = 0
blocks = []
for r in range(N):
    for c in range(M):
        if not visited[r][c] and is_blank[r][c]:
            cnt += 1
            blocks.append(bfs(r, c))

print(cnt)
blocks.sort()
print(" ".join(map(str, blocks)))