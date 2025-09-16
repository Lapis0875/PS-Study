input = open(0).readline

N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

max_x = 0
max_y = 0
for _ in range(N):
    x, y = map(int, input().split())
    max_x = max(max_x, x + 10)
    max_y = max(max_y, y + 10)
    for r in range(y, y + 10):
        for c in range(x, x + 10):
            board[r][c] += 1

surface = 0
for y in range(1, max_y + 1):
    for x in range(1, max_x + 1):
        surface += 1 if board[y][x] > 0 else 0

print(surface)