input = open(0).readline
N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
used = [False] * N
arr = [0] * M

def backtracking(depth, start):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for n in range(start, N):
        if not used[n]:
            used[n] = True
            arr[depth] = numbers[n]
            backtracking(depth + 1, n + 1)
            used[n] = False
    arr[depth] = ""

backtracking(0, 0)