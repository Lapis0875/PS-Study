from sys import stdin, exit

a, b, N, W = map(int, stdin.readline().split())

# x + y = N
# ax + by = W

# (a b) (W)
# (1 1) (N)

# (a b) (W)
# (a a) (aN)

# (a b) (W)
# (0 b - a) (W - aN)

# (a b) (W)
# (0 1) ((W - aN)/(b-a))

# (a 0) (W - b(W-aN)/(b-a))
# (0 1) ((W - aN)/(b-a))

# (1 0) ((bN - W)/(b-a))
# (0 1) ((W - aN)/(b-a))

if (d := b - a) == 0:
    if W // a == N:
        x = y = N // 2
        print(x, y)
    else:
        print(-1)
    exit(0)

y: float = (W - a * N) / d
x: float = N - y

if x <= 0 or y <= 0:
    print(-1)
elif x - int(x) != 0.0 or y - int(y) != 0.0:
    print(-1)
else:
    print(int(x), int(y))
