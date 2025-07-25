from collections import deque

input = open(0).readline
N, M = map(int, input().split())

# Union Find 알고리즘 구현
parent = [i for i in range(N + 1)]
def find_root(x):
    """x가 속한 분리 집합의 최상위 노드를 반환한다.
    분리 집합(트리)의 깊이를 줄이기 위해, 임의의 노드 x에 대해 최상위 노드를 탐색한 뒤 최상위 노드를 바로 부모 노드로 설정한다.
    """
    if parent[x] == x:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union_root(x, y):
    """x와 y가 속한 두 분리 집합을 병합한다."""
    root_x = find_root(x)
    root_y = find_root(y)

    if root_x != root_y:
        parent[root_y] = root_x

# Kruskal MST 알고리즘 구현
edges = sorted((tuple(map(int, input().split())) for _ in range(M)), key=lambda edge: edge[2]) # 전체 간선을 입력받은 뒤 가중치 기준으로 정렬한다.

# Kruskal 알고리즘
mst = deque()
total_cost = 0
for i in range(M):
    x, y, c = edges[i]

    if find_root(x) == find_root(y):
        continue    # 사이클이 발생하는 간선은 MST에 넣지 않는다.
        
    mst.append((x, y, c))
    total_cost += c
    union_root(x, y)

    if len(mst) == N - 1: # N개의 정점에 대해 N-1개의 간선을 찾았다면 MST를 완성한 것이니 탐색을 종료한다.
        break

# 최소 비용으로 두개의 도시를 만들기 위해서는, 현재 도시를 구성하는 MST를 만든 뒤 가장 비용이 높은 간선을 제거하면 된다.
print(total_cost - mst[N-2][2])