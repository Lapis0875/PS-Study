from collections import deque
input = open(0).readline
N = int(input())
TILE = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
diff = ((0, 1), (0, -1), (1, 0), (-1, 0)) # (dh, dw)

max_safe_areas = 1 # 최대 안전 영역 수
queue = deque()

def init():
    queue.clear()
    for h in range(N):
        for w in range(N):
            visited[h][w] = False

def bfs(h, w, rain_height):
    queue.append((h, w))
    visited[h][w] = True
    while queue:
        h, w = queue.popleft()
        for dh, dw in diff:
            nh, nw = h + dh, w + dw
            if 0 <= nh < N and 0 <= nw < N and not visited[nh][nw] and TILE[nh][nw] > rain_height:
                visited[nh][nw] = True
                queue.append((nh, nw))

def count_safe_areas(rain_height):
    cnt = 0
    # Find all possible entrances
    for h in range(N):
        for w in range(N):
            if not visited[h][w] and TILE[h][w] > rain_height:
                cnt += 1
                bfs(h, w, rain_height)
    return cnt

for i in range(1, 101):
    init()
    res = count_safe_areas(i)
    if res > max_safe_areas:
        max_safe_areas = res

print(max_safe_areas)