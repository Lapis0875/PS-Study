from collections import deque
input = open(0).readline
N = int(input())
edges = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

def bfs(start_node):
    visited = [-1 for _ in range(N + 1)]
    queue = deque()
    queue.append(start_node)
    visited = [-1 for _ in range(N + 1)]
    visited[start_node] = 0
    max_distance = 0
    max_node = 0
    while queue:
        cur_node = queue.popleft()

        if visited[cur_node] > max_distance:
            max_distance = visited[cur_node]
            max_node = cur_node

        for next_node, distance in edges[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + distance
                queue.append(next_node)
    return (max_node, max_distance)

# bfs (1) : 루트 정점(1)에서 가장 거리가 먼 정점 찾기 -> max_node
# bfs (2) : max_node에서 가장 거리가 먼 정점 찾기
max_node, _ = bfs(1)
_, max_distance = bfs(max_node)

print(max_distance)