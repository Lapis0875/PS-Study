input = open(0).readline
N, M = map(int, input().split())
A = sorted(map(int, input().split()))

visited = [False for _ in range(N)]
result = []
def dfs(depth):
    if depth == M:
        print(" ".join(map(str, result)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(A[i])
            dfs(depth + 1)
            visited[i] = False
            result.pop()

dfs(0)