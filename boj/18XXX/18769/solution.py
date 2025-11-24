input = open(0).readline

def find_root(roots, x):
    if roots[x] == x:
        return x
    roots[x] = find_root(roots, roots[x])
    return roots[x]

def union(roots, x, y):
    root_x = find_root(roots, x)
    root_y = find_root(roots, y)
    if root_x != root_y:
        roots[root_y] = root_x
        return True
    return False

def solution():
    R, C = map(int, input().split())
    edges = []
    for r in range(R):  # 수평 방향 간선 입력
        for idx, cost in enumerate(map(int, input().split())):
            u = r * C + idx
            v = u + 1
            edges.append((u, v, cost))
            edges.append((v, u, cost))
    for r in range(R - 1):  # 수직 방향 간선 입력
        for idx, cost in enumerate(map(int, input().split())):
            u = r * C + idx
            v = u + C
            edges.append((u, v, cost))
            edges.append((v, u, cost))
    edges.sort(key=lambda x: x[2])  # 비용 기준으로 정렬

    roots = [i for i in range(R * C)]  # Union-Find 초기화 / 0부터 R x C - 1까지의 정점 번호 사용
    total_cost = 0
    total_edges = 0
    for u, v, cost in edges:
        if union(roots, u, v):
            total_cost += cost
            
        if total_edges == R * C - 1:  # 모든 정점이 연결되면 종료
            break
    print(total_cost)

for _ in range(int(input())):
    solution()