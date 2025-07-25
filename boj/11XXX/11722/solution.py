input = open(0).readline
N = int(input().strip())
A = list(map(int, input().strip().split()))

dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if A[j] < A[i]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))