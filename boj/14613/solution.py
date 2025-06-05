input = open(0).readline
W, L, D = map(float, input().split())

# DP?
# 지금까지 플레이 한 판 수 / 현재 점수의 2가지 변수로 DP 배열 구성하기

RESULTS = [0.0 for _ in range(5)]  # 브 실 골 플 다
DP = [[0.0 for _ in range(3501)] for _ in range(21)]
DP[0][2000] = 1.0

for i in range(1, 21):
    for j in range(0, 3501, 50):   # 어짜피 50점 단위로 변화한다.
        if DP[i - 1][j] > 0:
            # 승리
            DP[i][j + 50] += DP[i - 1][j] * W
            # 패배
            DP[i][j - 50] += DP[i - 1][j] * L
            # 무승부
            DP[i][j] += DP[i - 1][j] * D

for i in range(0, 3501, 50):
    if 1000 <= i < 1500:
        RESULTS[0] += DP[20][i]
    elif 1500 <= i < 2000:
        RESULTS[1] += DP[20][i]
    elif 2000 <= i < 2500:
        RESULTS[2] += DP[20][i]
    elif 2500 <= i < 3000:
        RESULTS[3] += DP[20][i]
    elif 3000 <= i < 3500:
        RESULTS[4] += DP[20][i]

for i in range(5):
    print(f"{RESULTS[i]:.8f}")
