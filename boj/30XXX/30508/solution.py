from collections import deque
input = open(0).readline

NEXT_POS = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
H, W = map(int, input().split())
tiles = [[None] for _ in range(N + 1)]
drained = [[False] * (M + 1) for _ in range(N + 1)]
prefix = [[0] * (M + 1) for _ in range(N + 1)]
queue = deque()

# 0. 입력 받기
for i in range(1, N + 1):
    tiles[i].extend(map(int, input().split()))

def bfs(r, c):
    queue.clear()
    queue.append((r, c))
    drained[r][c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in NEXT_POS:
            nr = r + dr
            nc = c + dc
            if 1 <= nr <= N and 1 <= nc <= M and not drained[nr][nc] and tiles[nr][nc] >= tiles[r][c]:
                drained[nr][nc] = True
                queue.append((nr, nc))
    
# 1. 하수구에서부터 BFS 진행해서 전체 타일에 물이 빠진 칸 파악하기
for _ in range(int(input())):
    r, c = map(int, input().split())
    bfs(r, c)

# 2. 누적합 계산해서 (r, c) 지점까지 물이 빠진 칸의 수 세기
for r in range(1, N + 1):
    for c in range(1, M + 1):
        prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1] + (1 if drained[r][c] else 0)

# 3. H x M 크기로 모두 물이 빠진 칸이 몇 개 존재하는지 계산하기
size = H * W
count = 0
for r in range(1, N - H + 2):
    for c in range(1, M - W + 2):
        drained_tiles = prefix[r + H - 1][c + W - 1] - prefix[r - 1][c + W - 1] - prefix[r + H - 1][c - 1] + prefix[r - 1][c - 1]
        if drained_tiles >= size:
            count += 1

print(count)