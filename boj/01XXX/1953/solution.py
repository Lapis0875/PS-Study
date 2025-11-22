from collections import deque
input = open(0).readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    E, *verticies = map(int, input().rstrip().split())
    for v in verticies:
        graph[i].append(v)
        graph[v].append(i)

# BFS로 이분 그래프 색칠하기
team_number = [0] * (N + 1)
queue = deque()
def bfs(src):
    queue.clear()
    queue.append(src)
    team_number[src] = 1
    is_bipartite = True
    while is_bipartite and queue:
        u = queue.popleft() # 정점의 깊이를 기준으로 
        for v in graph[u]:
            if team_number[v] == 0: # 새로 방문하는 정점
                team_number[v] = -team_number[u]
                queue.append(v)
            elif team_number[v] + team_number[u] != 0: # 이분 그래프가 아니게 되는 경우: 인접한 정점과 같은 색으로 칠해질 때
                is_bipartite = False
                break
    return is_bipartite

for i in range(1, N + 1):
    if team_number[i] == 0:
        bfs(i)

team_members = ([], [])
for i in range(1, N + 1):
    if team_number[i] == 1:
        team_members[0].append(i)
    else:
        team_members[1].append(i)

print(f"{len(team_members[0])}\n{' '.join(map(str, team_members[0]))}\n{len(team_members[1])}\n{' '.join(map(str, team_members[1]))}")
