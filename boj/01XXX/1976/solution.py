input = open(0).readline
N = int(input())
M = int(input())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# Disjoint Set (Union-Find)
parent = [i for i in range(N + 1)]
def find(x):
    path = []
    while x != parent[x]:
        path.append(x)
        x = parent[x]
    for p in path:
        parent[p] = x
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False

for i in range(1, N + 1):
    for j, connected in enumerate(map(int, input().split()), start=1):
        graph[i][j] = connected
        if connected == 1:
            union(i, j)

plan = list(map(int, input().split()))
for v in range(1, M):
    if find(plan[v - 1]) != find(plan[v]):
        print("NO")
        break
else:
    print("YES")
