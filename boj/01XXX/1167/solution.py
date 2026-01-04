from collections import deque
input = open(0).readline
V = int(input())
edges = tuple([] for _ in range(100_001))

for _ in range(V):
    edge_inputs = map(int, input().split())
    u = next(edge_inputs)
    while edge_inputs:
        v = next(edge_inputs)
        if v == -1:
            break
            
        w = next(edge_inputs)
        edges[u].append((v, w))
        edges[v].append((u, w))

queue = deque()

def bfs(start_node):
    visited = [-1] * (V + 1)
    visited[start_node] = 0
    queue.clear()
    queue.append(start_node) # (정점, 거리)
    max_distance = 0
    deepest_node = start_node

    while queue:
        cur_node = queue.popleft()
        for next_node, weight in edges[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + weight
                queue.append(next_node)
                if visited[next_node] > max_distance:
                    max_distance = visited[next_node]
                    deepest_node = next_node
    return deepest_node, max_distance

before_node = 1
root_node = 1

# bfs (1) : 루트 정점(1)에서 가장 거리가 먼 정점 찾기 -> max_node
# bfs (2) : max_node에서 가장 거리가 먼 정점 찾기
max_node, _ = bfs(1)
_, max_distance = bfs(max_node)

print(max_distance)