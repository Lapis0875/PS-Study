from collections import deque
input = open(0).readline
N, K = map(int, input().split())
if N == K:
    print("0\n1")
else:
    queue = deque((N, ))
    visited = [-1 for _ in range(100001)]
    visited[N] = 0
    count = 0
    while queue:
        x = queue.popleft()
        # 이미 K에 도달한 경우보다 더 오랜 시간 탐색하는 경우는 무시한다.
        if visited[K] != -1 and visited[K] < visited[x] + 1:
            continue
        # 다음 경우를 큐에 넣는다.
        for nx in (x - 1, x + 1, x * 2):
            # 방문하지 않았거나, 현재 위치에서 K에 도달하는 시간이 더 짧거나 같은 경우
            if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] >= visited[x] + 1):
                visited[nx] = visited[x] + 1
                if nx == K:
                    count += 1
                queue.append(nx)

    print(visited[K])
    print(count)