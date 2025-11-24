from collections import deque
input = open(0).readline

color = [0] * 20001 # 1 <= V <= 20,000
graph = []

def bfs(src, src_color):
    """너비 우선 탐색(BFS)을 통해 주어진 그래프가 이분 그래프인지 판단한다.
    Arguments:
        src (int): 탐색 시작 정점
        color (Literal[-1, 1]): 시작 정점의 색상. 정점의 색상은 1 또는 -1로 표현한다.
    
    Returns:
        bool: 현재 정점에서 출발해 주어진 그래프를 탐색했을 때, 이 그래프가 이분 그래프인지 아닌지의 여부를 반환한다.
    """
    queue = deque([src])
    color[src] = src_color
    is_bipartite = True # 이분 그래프인지 여부를 기록하는 변수
    while queue and is_bipartite:
        u = queue.popleft()
        for v in graph[u]:
            if color[v] == 0: # 아직 방문하지 않은 정점일 경우, 새로 색칠한 후 탐색을 이어간다.
                color[v] = color[u] * -1
                queue.append(v)
            elif color[v] + color[u] != 0: # 인접한 두 정점이 같은 색으로 칠해진 경우, 이분 그래프가 아니다!
                is_bipartite = False
                break
    return is_bipartite


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph.clear()
    for i in range(V + 1):
        color[i] = 0 # 초기화 값. 이후 그래프 탐색을 통해 1 또는 -1로 칠해진다.
        graph.append([])
    
    # 인접한 두 정점의 번호를 입력으로 제공받는다.
    # 양방향 연결로 간주한다.
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS로 그래프를 탐색한다.
    # 각 탐색의 깊이에 따라 2가지 색을 번갈아 가며 각 정점에 칠한다.
    # 만약 기존에 칠해진 정점의 색과 다른 색으로 칠하게 되는 경우가 발생할 시 -> 이분 그래프가 아니다!
    is_bipartite = True
    for i in range(1, V + 1):
        if color[i] == 0:
            is_bipartite = bfs(i, 1)
            # 항상 1로 칠해도 되는가? 에 대한 고찰
            # 이전 BFS에서 칠해지지 않은 정점이라는 것은 이전에 탐색한 부분 그래프와 현재 정점이 서로 연결되지 않았다는 뜻이다.
            # 따라서, 새 정점을 탐색할 때 이를 어떤 색으로 칠하든 다른 부분 그래프에는 영향이 없다.
            # 일관되게 출발 정점을 1로 칠하는 것.
        if not is_bipartite:
            break

    print("YES" if is_bipartite else "NO")
