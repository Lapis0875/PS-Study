input = open(0).readline
N = int(input())
A = list(map(int, input().split()))

increasing = [1] * N
decreasing = [1] * N

# 증가하는 수열(LIS)은 좌측에서 시작하므로 정방향으로 탐색한다.
for i in range(N):
    for j in range(i + 1, N):
        if A[j] > A[i]:
            increasing[j] = max(increasing[j], increasing[i] + 1)

# 감소하는 수열(LDS)은 우측에서 시작하므로 역방향으로 탐색한다.
for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if A[j] > A[i]: # LDS를 역방향으로 탐색하므로, 점점 커지는 방향으로 수를 찾게 된다.
            decreasing[j] = max(decreasing[j], decreasing[i] + 1)

# 임의의 중점을 잡고 양방향에서 LIS + LDS를 했을 때 그 길이가 최대가 되는 것을 찾는다.
# LIS와 LDS도 바이토닉 수열의 일종이다.
max_length = 1
for i in range(N):
    max_length = max(max_length, increasing[i] + decreasing[i] - 1) # increasing[i]와 decreasing[i] 모두 i를 포함하므로 1 뺀다.

print(max_length)