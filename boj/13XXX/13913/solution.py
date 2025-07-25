from collections import deque
input = open(0).readline
N, K = map(int, input().strip().split())
    
if K < N:   # 수빈이가 동생보다 큰 위치에 있다면
    print(N - K)
    print(" ".join(map(str, range(N, K - 1, -1))))
elif K == N:
    print("0")
    print(N)
else:
    queue = deque([[N]])
    visited = [-1 for _ in range(200_002)]
    visited[N] = 0
    while queue:
        current = queue.popleft()
        if current[-1] == K:
            print(visited[current[-1]])
            print(" ".join(map(str, current)))
            break

        for next in (current[-1] * 2, current[-1] - 1, current[-1] + 1):
            if 0 <= next <= 200_000 and visited[next] == -1:
                visited[next] = visited[current[-1]] + 1
                next_path = current.copy()
                next_path.append(next)
                queue.append(next_path)
    