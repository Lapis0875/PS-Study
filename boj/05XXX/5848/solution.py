input = open(0).readline

N = int(input())
F = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(n):
    if F[n] == 0:
        return False # 탐색 종료, 사이클 X

    if not visited[F[n]]:
        visited[F[n]] = True
        return dfs(F[n])
    else:
        return True # 탐색 종료, 사이클 O

for i in range(1, N + 1):
    F[i] = int(input())

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        visited[j] = False
    visited[i] = True
    res = dfs(i)
    if not res:
        cnt += 1

print(cnt)
