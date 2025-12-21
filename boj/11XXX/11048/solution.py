input = open(0).readline

N, M = map(int, input().split())
maze = tuple(tuple(map(int, input().split())) for _ in range(N))

dp = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        dp[r][c] = maze[r][c]

        if r > 0:
            dp[r][c] = max(dp[r][c], dp[r - 1][c] + maze[r][c])
            if c > 0:
                dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + maze[r][c])
        if c > 0:
            dp[r][c] = max(dp[r][c], dp[r][c - 1] + maze[r][c])

print(dp[N - 1][M - 1])