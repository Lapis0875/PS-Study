input = open(0).readline
N = int(input())
planets = [(idx,) + tuple(map(int, input().split())) for idx in range(N)]

# Kruskal 알고리즘을 사용하기 위해 간선을 만든 뒤 가중치의 크기 순으로 오름차순 정렬한다.
# https://www.acmicpc.net/board/view/145011
# 결국 최소 거리로 두 행성을 연결하는 경우는, x/y/z 3개 중 1개 축에서 인접하는 행성끼리 연결하는 경우 뿐이다.
# 1차원 좌표들로 MST를 만들면 일직선으로 형성된다는 점을 3차원으로 확장해보면 된다.

edges = []
for axis in range(1, 4):
    axis_sorted = sorted(planets, key=lambda p: p[axis])
    for i in range(N - 1):
        weight = abs(axis_sorted[i][axis] - axis_sorted[i + 1][axis])
        edges.append((axis_sorted[i][0], axis_sorted[i + 1][0], weight))

edges.sort(key=lambda e: e[2])

# Union Find 알고리즘
parents = [i for i in range(N)]

def find_parent(vertex):
    """어떤 정점(vertex)이 속한 분리 집합의 최상위 노드를 반환한다.
    분리 집합(트리)의 깊이를 줄이기 위해, 임의의 노드 x에 대해 최상위 노드를 탐색한 뒤 최상위 노드를 바로 부모 노드로 설정한다.
    """
    if vertex == parents[vertex]:
        return vertex
    parents[vertex] = find_parent(parents[vertex])
    return parents[vertex]

def union(vertex_a, vertex_b):
    """두 정점 vertex_a와 vertex_b가 속한 두 분리 집합을 병합한다."""
    parent_a = find_parent(vertex_a)
    parent_b = find_parent(vertex_b)

    if parent_a != parent_b:
        parents[parent_b] = parent_a

# Kruskal 알고리즘
mst_len = 0
total_cost = 0
for x, y, c in edges:
    if find_parent(x) == find_parent(y):    # 사이클이 생기는 간선은 MST에 추가해선 안된다.
        continue
    mst_len += 1
    total_cost += c
    union(x, y)

    if mst_len == N - 1:   # MST는 항상 N개의 정점을 가지는 그래프에 대해 N-1개의 간선을 가지는 트리이다.
        break

print(total_cost)