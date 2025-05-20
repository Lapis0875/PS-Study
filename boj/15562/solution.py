input = open(0).readline
N, M = map(int, input().split())
array = [0 for _ in range(M)]

def dfs(depth, prev):
    if depth == M:
        print(" ".join(map(str, array)))
        return
    for i in range(prev, N + 1):
        array[depth] = i
        dfs(depth + 1, i)
        array[depth] = 0

dfs(0, 1)
