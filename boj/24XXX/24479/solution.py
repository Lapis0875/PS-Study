from sys import setrecursionlimit
input = open(0).readline

setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

graph = tuple([] for _ in range(N + 1))
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for u in range(1, N + 1):
    graph[u].sort()

visited = [0] * (N + 1)
visit_cnt = 1
def dfs(node):
    global visit_cnt
    for next_node in graph[node]:
        if visited[next_node] == 0:
            visit_cnt += 1
            visited[next_node] = visit_cnt
            dfs(next_node)

visited[R] = 1
dfs(R)
for i in range(1, N + 1):
    print(visited[i])
