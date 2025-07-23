from decimal import getcontext, ROUND_HALF_UP, Decimal
input = open(0).readline
getcontext().rounding = ROUND_HALF_UP

N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]
base_x, base_y = coords[0]

surface = 0
for i in range(1, N - 1):
    # CCW
    vec1_x = coords[i][0] - base_x
    vec1_y = coords[i][1] - base_y
    vec2_x = coords[i + 1][0] - base_x
    vec2_y = coords[i + 1][1] - base_y
    surface += vec1_x * vec2_y - vec2_x * vec1_y

print(round(Decimal(abs(surface) / 2), 1))