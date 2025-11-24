input = open(0).readline

# Union Find

roots = [i for i in range(30001)]
ranks = [0 for _ in range(30001)]

def find_root(node):
    path = []
    while node != roots[node]:
        path.append(node)
        node = roots[node]
    for p in path:
        roots[p] = node
    return node

def union(node_x, node_y):
    root_x = find_root(node_x)
    root_y = find_root(node_y)

    if root_x == root_y: # same parent
        return False
    
    if ranks[root_x] < ranks[root_y]:
        roots[root_x] = root_y
    else:
        roots[root_y] = roots[root_x]

        if ranks[root_x] == ranks[root_y]:
            ranks[root_x] += 1
    return True

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# Connect all nodes based on edge information.
for i in range(1, N + 1):
    for j in edges[i]:
        union(i, j)

# Convert problem to knapsack problem: Each graph => single item (weight = children count, value = total candies)
items_total = {}
for i in range(1, N + 1):
    root = find_root(i)
    try:
        items_total[root][0] += 1
        items_total[root][1] += candies[i - 1]
    except KeyError:
        items_total[root] = [1, candies[i - 1]] # (weight, value)
items = [(0, 0), *items_total.values()]

DP = [[0 for _ in range(K)] for _ in range(len(items))] # DP[item_idx][weight_left]

for i in range(1, len(items)):
    for w in range(K):
        if items[i][0] <= w:
            DP[i][w] = max(DP[i-1][w], items[i][1] + DP[i-1][w-items[i][0]])
        else:
            DP[i][w] = DP[i-1][w]

print(DP[len(items) - 1][K - 1])