from collections import deque
input = open(0).readline
N = int(input())
edges = tuple([] for _ in range(N + 1))

for _ in range(N):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# BFS
color = [-1 for _ in range(N + 1)]
queue = deque([1])
color_cnt = 2 # 최소한 2개의 색상은 필요하다.
color[1] = 0

while queue:
    pos = queue.popleft()

    for other in edges[pos]:
        if color[other] == -1: # 방문하지 않은 경우
            color[other] = (color[pos] + 1) % color_cnt
            queue.append(other)
        elif color[other] == color[pos]: # 색상 중복 시
            color[other] = color_cnt
            color_cnt += 1

print(color_cnt)
