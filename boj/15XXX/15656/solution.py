input = open(0).readline
N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))
arr = [0] * M

def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for n in range(N):
        arr[depth] = numbers[n]
        backtracking(depth + 1)
    arr[depth] = ""

backtracking(0)