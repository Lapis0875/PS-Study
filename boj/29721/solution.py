input = open(0).readline
N, K = map(int, input().split())

visited = {}
dabbabas = []

for i in range(K):
    x, y = map(lambda n: int(n) - 1, input().split())
    visited[(x, y)] = True
    dabbabas.append((x, y))

cnt = 0
for x, y in dabbabas:
    for dx, dy in ((2, 0), (0, 2), (0, -2), (-2, 0)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited.get((nx, ny), False):
            cnt += 1
            visited[(nx, ny)] = True

print(cnt)