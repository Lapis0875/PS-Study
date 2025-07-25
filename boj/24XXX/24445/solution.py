from sys import stdin

N, M, R = map(int, stdin.readline().split())
visited = [0 for _ in range(N + 1)]             # 방문 여부 리스트. 정점은 1부터 N까지 존재하므로 N+1 크기로 초기화.

graph = [[] for _ in range(N + 1)]                  # 인접 리스트. 정점은 1부터 N까지 존재하므로 N+1 크기로 초기화.
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)                              # u에서 v로 가는 간선 추가
    graph[v].append(u)                              # v에서 u로 가는 간선 추가 (무향 그래프이므로 양방향)

for edges in graph:
    edges.sort(reverse=True)                        # 인접 리스트를 내림차순으로 정렬하여 DFS 순서를 결정한다.

visited[R] = 1                                      # 시작 정점 R을 방문 처리.
queue = [R]                                         # BFS를 위해 방문 예정 정점 큐를 초기화.
order = 2
while queue:
    node = queue.pop(0)                             # 큐에서 정점 하나를 꺼낸다.
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = order                      # 정점 n을 방문 처리.
            queue.append(n)                         # 정점 n을 큐에 추가.
            order += 1

for i in range(1, N + 1):
    print(visited[i])                               # 방문 순서 출력. visited[i]는 정점 i의 방문 순서.
