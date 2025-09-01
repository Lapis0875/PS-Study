from collections import deque
input = open(0).readline

N, M = map(int, input().split())
in_degree = [0 for _ in range(N + 1)]
edges = [[] for _ in range(N + 1)]
result = [0 for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    in_degree[v] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

for i in range(N):
    if len(queue) == 0:
        break

    cur = queue.popleft()
    result[i] = cur

    for next in edges[cur]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

print(*result)