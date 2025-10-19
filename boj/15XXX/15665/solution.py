input = open(0).readline
N, M = map(int, input().split())
numbers = [False] * 10001
for n in map(int, input().split()):
    numbers[n] = True
arr = [0] * M

def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for n in range(10001):
        if numbers[n]:
            arr[depth] = n
            backtracking(depth + 1)
    arr[depth] = ""

backtracking(0)