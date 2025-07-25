input = open(0).readline
N = int(input())
pyramid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = pyramid[0][0]

for i in range(1, N): # 다음 층의 dp 배열을 계산한다.
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + pyramid[i][j] # 무조건 오른쪽밖에 못가는 경우
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + pyramid[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + pyramid[i][j]

print(max(dp[N - 1]))
