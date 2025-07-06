input = open(0).readline
N, M = map(int, input().split())
arr = [[2 for _ in range(M + 1)] for _ in range(N + 1)] # 0이면 노란 꽃, 1이면 빨간 꽃. 2는 둘다 아닌 기본 값.

# 가장자리에 이미 심어져 있는 꽃 입력받기
for i, flower in zip(range(1, N + 1), map(int, input().split())):
    arr[i][0] = flower

# 가장자리에 이미 심어져 있는 꽃 입력받기
for i, flower in zip(range(1, M + 1), map(int, input().split())):
    arr[0][i] = flower

for r in range(1, N + 1):
    for c in range(1, M + 1):
        arr[r][c] = 0 if arr[r-1][c] == arr[r][c-1] else 1

# print("\n".join(map(lambda row: ' '.join(map(str, row)), arr)))
# print()

print(arr[N][M])
