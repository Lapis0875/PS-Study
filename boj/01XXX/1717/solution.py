input = open(0).readline
N, M = map(int, input().split())

# Union-Find
parents = [i for i in range(N + 1)]

def find_parent(x):
    path = []
    while x != parents[x]:
        path.append(x)
        x = parents[x]
    for p in path:
        parents[p] = x
    return x

def union(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)

    if parent_x != parent_y:
        parents[parent_y] = parent_x

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        print("YES" if find_parent(a) == find_parent(b) else "NO")
