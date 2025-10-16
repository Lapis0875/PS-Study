from collections import deque
input = open(0).readline

arr = [0] * 1001
roots = [0] * 1001
visited = [False] * 1001
queue = deque()

# Union - Find
def find_root(x):
    path = [] # 분리 집합 트리 탐색 경로 기록
    while x != roots[x]:
        path.append(x)
        x = roots[x]
    # 트리 평탄화 (탐색 깊이 줄이기)
    for p in path:
        roots[p] = x
    return x

def union(x, y):
    x = find_root(x)
    y = find_root(y)

    if x == y: # 이미 같은 집합에 속한다.
        return False
    # 단순하게 x쪽으로 병합
    roots[y] = x

# BFS
def bfs(i):
    queue.clear()
    queue.append(i)
    visited[i] = True

    while queue:
        i = queue.popleft()
        if not visited[arr[i]]:
            queue.append(arr[i])
            union(i, arr[i])
            visited[arr[i]] = True

for _ in range(int(input())):
    N = int(input())
    for i, v in enumerate(map(int, input().split()), 1):
        arr[i] = v
        roots[i] = i
        visited[i] = False
    
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
    
    cnt = 0
    for i in range(1, N + 1):
        if roots[i] == i:
            cnt += 1
    print(cnt)
