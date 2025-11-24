from sys import setrecursionlimit
setrecursionlimit(10**5)
input = open(0).readline
preferred_teams = [0] * 100_001 # 전역 변수로 선언
visited = [False for _ in range(100_001)]
teamed_cnt = 0

def dfs(n, depth, path):
    print(f"DFS({n}): Depth {depth} / Path {path[:depth + 1]}")
    
    next_n = preferred_teams[n]
    if not visited[next_n]:
        visited[next_n] = True
        path[depth + 1] = next_n
        dfs(next_n, depth + 1, path)
        path[depth + 1] = 0
    else:
        for prev in range(depth):
            if path[prev] == next_n:
                global teamed_cnt
                teamed_cnt += depth + 1 - prev
                print(f"DFS({n}): Cycle Found! {depth + 1 - prev} / {path[:depth + 1]}")
                return
        

def solution():
    global teamed_cnt
    N = int(input())
    teamed_cnt = 0
    for idx, value in enumerate(map(int, input().split()), 1):
        preferred_teams[idx] = value
        visited[idx] = False
        if idx == value: # 자기 자신을 팀으로 선호하는 경우는 즉시 사이클을 판단할 수 있으므로 사전에 처리해 둔다.
            visited[idx] = True
            teamed_cnt += 1
    
    path = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            path[0] = i
            dfs(i, 0, path)
    
    print(N - teamed_cnt)

for _ in range(int(input())):
    solution()