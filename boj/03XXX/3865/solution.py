from collections import deque
input = open(0).readline

cnt = 0
edges = {}
visited = {}
target_academy = ""
queue = deque()
while True:
    N = int(input())
    if N == 0:
        break

    cnt = 0
    edges.clear()
    visited.clear()
    for i in range(N):
        text = input().rstrip()[:-1]
        academy_name, member_names = text.split(":")
        if i == 0:
            target_academy = academy_name
        edges[academy_name] = member_names.split(",")

    # BFS to resolve member count
    queue.append(target_academy)
    while queue:
        name = queue.popleft()
        for m in edges[name]:
            if not visited.get(m, False):
                visited[m] = True
                if edges.get(m, None) is not None and len(edges[m]) > 0:
                    queue.append(m)
                else:
                    cnt += 1
    print(cnt)
