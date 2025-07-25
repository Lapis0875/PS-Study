from collections import deque
input = open(0).readline
N, K = map(int, input().strip().split())

queue = deque([N])
visited = [-1 for _ in range(200_002)]
visited[N] = 0
while queue:
    current = queue.popleft()
    if current == K:
        print(visited[current])
        break

    for next, time in ((current * 2, visited[current]), (current - 1, visited[current] + 1), (current + 1, visited[current] + 1)):
        if visited[next] == -1 and 0 <= next <= 100_000:
            visited[next] = time
            queue.append(next)
    