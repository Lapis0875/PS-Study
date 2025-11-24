input = open(0).readline
N, M = map(int, input().split())

path = ["" for _ in range(M)]
def backtracking(depth):
    if depth == M:
        print(" ".join(path))
        return
    
    for i in range(1, N + 1):
        path[depth] = str(i)
        backtracking(depth + 1)
    path[depth] = ""

backtracking(0)