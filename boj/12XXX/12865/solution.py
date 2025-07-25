input = open(0).readline
N, K = map(int, input().split())
items = tuple(tuple(map(int, input().split())) for _ in range(N))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = items[i - 1]
    for w in range(K + 1):
        if weight <= w: # 가방에 현재 물건을 담을 수 있는 경우.
            # 현재 물건을 담지 않는 경우와 담는 경우 중 최대값을 선택
            dp[i][w] = max(dp[i-1][w], value + dp[i-1][w-weight])
        else: # 가방에 현재 물건을 담을 수 없는 경우.
            dp[i][w] = dp[i-1][w]

print(dp[N][K])