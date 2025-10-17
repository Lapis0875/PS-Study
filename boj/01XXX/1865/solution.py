input = open(0).readline

edges = []
distance = [0] * 501

def bellman_ford(V):
    # 모든 정점의 거리를 0으로 설정
    # 가상의 정점 V+1에서 출발한다고 가정하고, V+1에서 다른 모든 정점으로 거리가 0인 간선을 그어 모든 정점에서 출발 가능하도록 설정한다.
    # 이는 벨만-포드 알고리즘이 1개 정점에서 다른 모든 정점으로의 최단 경로를 탐색하기 때문이며,
    # 따라서 출발점에서 도달할 수 없는 정점에 있는 음의 사이클을 찾지 못하기 때문이다.
    # 단순히 1~V까지의 모든 정점에서 출발하도록 하면, 시간 복잡도가 O(N^2 * M)꼴로 매우 느려지기 때문에
    # 차라리 가상의 정점을 만들어 모든 정점에서 동시에 출발하도록 구현하는 편이 시간 면에서 유리하다.
    for i in range(1, V + 1):
        distance[i] = 0
    for _ in range(V - 1):
        for s, e, t in edges:
            if distance[s] + t < distance[e]:
                distance[e] = distance[s] + t
    
    # 음의 사이클 유무 판단하기: 최단경로는 V-1개의 간선으로 이루어진다고 가정.
    for s, e, t in edges:
        if distance[s] + t < distance[e]:
            return True # 음의 사이클 존재
    return False        # 음의 사이클 없음

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges.clear()
    
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    print("YES" if bellman_ford(N) else "NO")
