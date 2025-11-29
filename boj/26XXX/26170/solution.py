input = open(0).readline
tiles = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
NEXT = ((1, 0), (0, 1), (-1, 0), (0, -1))
start = tuple(map(int, input().split()))

min_dist = 26

def dfs(depth, collected, r, c):
    global min_dist
    if collected == 3:
        if depth <= min_dist: # 최단 거리가 갱신된 경우
            min_dist = depth
        return
    
    for dr, dc in NEXT:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and tiles[nr][nc] != -1 and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(depth + 1, collected + tiles[nr][nc], nr, nc)
            visited[nr][nc] = False

visited[start[0]][start[1]] = True
dfs(0, 0, *start)
print(min_dist if min_dist < 26 else -1)