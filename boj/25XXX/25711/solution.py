from decimal import Decimal
input = open(0).readline

N, Q = map(int, input().split())
DECIMAL_SQRT = Decimal("0.5")

def calculate_health(prev_y, cur_y, distance):
    height_diff = cur_y - prev_y
    if height_diff == 0:
        return distance * 2
    elif height_diff > 0:
        return distance * 3
    else: # height_diff < 0
        return distance

X = list(map(Decimal, input().split()))
Y = list(map(Decimal, input().split()))

prefix_health = [0] * N # x좌표가 증가하는 방향으로 이동시의 누적 합
reversed_prefix_health = [0] * N # x좌표가 감소하는 방향으로 이동 시의 누적 합

for idx in range(1, N):
    distance = ((X[idx] - X[idx - 1]) ** 2 + (Y[idx] - Y[idx - 1]) ** 2) ** DECIMAL_SQRT
    prefix_health[idx] = prefix_health[idx - 1] + calculate_health(Y[idx - 1], Y[idx], distance)

    rev_idx = N - 1 - idx
    distance = ((X[rev_idx + 1] - X[rev_idx]) ** 2 + (Y[rev_idx + 1] - Y[rev_idx]) ** 2) ** DECIMAL_SQRT
    reversed_prefix_health[rev_idx] = reversed_prefix_health[rev_idx + 1] + calculate_health(Y[rev_idx + 1], Y[rev_idx], distance)

for _ in range(Q):
    i, j = map(int, input().split())
    if i <= j:
        # 칸을 기준으로 누적 합을 계산했으므로, i번째 칸 ~ j-1번째 칸까지의 합을 계산한다.
        dist = prefix_health[j - 1] - prefix_health[i - 1]
    else:
        # 칸을 기준으로 누적 합을 계산했으므로, i - 1번째 칸 ~ j번째 칸까지의 합을 계산한다.
        dist = reversed_prefix_health[j - 1] - reversed_prefix_health[i - 1]
    print(f"{dist:f}")
