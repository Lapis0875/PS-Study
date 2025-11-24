from collections import deque

input = open(0).readline

N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

queue = deque([(0, 0)])
visited[0][0] = True

while queue:
    r, c = queue.popleft()
    jump = maze[r][c]
    
    if jump == 0:
        continue

    # 아래로
    dr = r + jump
    dc = c
    if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
        visited[dr][dc] = True
        queue.append((dr, dc))

    # 오른쪽으로
    dr = r
    dc = c + jump
    if 0 <= dr < N and 0 <= dc < N and not visited[dr][dc]:
        visited[dr][dc] = True
        queue.append((dr, dc))

print("HaruHaru" if visited[N-1][N-1] else "Hing")