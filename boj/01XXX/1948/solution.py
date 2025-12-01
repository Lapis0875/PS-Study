from collections import deque

input = open(0).readline
N = int(input())
M = int(input())
graph = [[] for _ in range(10001)]
backward = [[] for _ in range(10001)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    backward[v].append((u, w))

start, end = map(int, input().split())
queue = deque([start])
time = [-1] * 10001
path = [[] for _ in range(10001)]
time[start] = 0

# 1. 최장 경로 구하기
max_time = 0
while queue:
    prev = queue.popleft()
    
    for v, w in graph[prev]:
        if time[v] == -1 or time[v] < time[prev] + w: # 처음 방문하거나 더 긴 시간에 도달한 경우 새로 기록한다. 우리는 최장경로가 필요함.
            time[v] = time[prev] + w
            if max_time < time[v]:
                max_time = time[v]
            queue.append(v)

# 2. 역추적으로 경로에 포함되는 간선의 개수 구하기
queue.append(end)
cnt = 0 # 최장 경로에 포함되는 간선의 개수.
# 같은 간선을 중복으로 방문할 수 있다. 이를 처리해야 함.
visited = [[False] * 10001 for _ in range(10001)]
while queue:
    now = queue.popleft()
    for prev, w in backward[now]:
        if time[now] == time[prev] + w and not visited[prev][now]:
            cnt += 1
            visited[prev][now] = True
            queue.append(prev)

print(f"{max_time}\n{cnt}")