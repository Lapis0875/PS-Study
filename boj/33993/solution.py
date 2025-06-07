input = open(0).readline
N, R, C, W = map(int, input().split())
SEATS = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(N):
    x, y = map(int, input().split())
    SEATS[x][y] = 1
# 누적 합 계산
# prefix_sum[y][x]는 (1,1)부터 (x, y)까지의 모든 좌석의 인원수의 합이다. (누적합)
prefix_sum = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for r in range(1, R + 1):
    for c in range(1, C + 1):
        prefix_sum[r][c] = prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1] + SEATS[r][c]
result_sum = 0
result_x = C + 1
result_y = R + 1
half = W >> 1
for x in range(1, R + 1):
    for y in range(1, C + 1):
        if SEATS[x][y] != 0: # 이미 친구가 앉아 있는 자리이므로 사용 불가.
            continue
        left = max(y - half, 1)
        right = min(y + half, C)
        up = max(x - half, 1)
        down = min(x + half, R)
        total = prefix_sum[down][right] - prefix_sum[up - 1][right] - prefix_sum[down][left - 1] + prefix_sum[up - 1][left - 1]   # 중복으로 빼진 부분은 다시 더한다.
        if total > result_sum or total == result_sum and ((x < result_x) or (x == result_x and y < result_y)):
            result_sum = total
            result_x = x
            result_y = y
print(f"{result_sum}\n{result_x} {result_y}")