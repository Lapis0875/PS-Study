input = open(0).readline
V, E = map(int, input().split())
edges = sorted((tuple(map(int, input().split())) for _ in range(E)), key=lambda e: e[2])

# Union-Find
parents = [i for i in range(V + 1)]

def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)

    if parent_x != parent_y:
        parents[parent_y] = parent_x
        return True
    return False

# Kruskal
total_weight = 0
for x, y, w in edges:
    if union(x, y):
        total_weight += w

print(total_weight)