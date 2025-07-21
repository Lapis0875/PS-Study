input = open(0).readline
P = [tuple(map(int, input().split())) for _ in range(3)]

# D = x1y2 + x2y3 + x3y1 - y1x2 -y2x3 - y3x1
D = P[0][0] * P[1][1] + P[1][0] * P[2][1] + P[2][0] * P[0][1] - P[0][1] * P[1][0] - P[1][1] * P[2][0] - P[2][1] * P[0][0]

if D > 0:
    print(1)
elif D < 0:
    print(-1)
else:
    print(0)