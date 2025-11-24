input = open(0).readline
N, M = map(int, input().split())
numbers_cnt = [0] * 10001
for n in map(int, input().split()):
    numbers_cnt[n] += 1
numbers_used = [0] * 10001
arr = [0] * M

def backtracking(depth, start):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for n in range(start, 10001):
        if numbers_used[n] < numbers_cnt[n]:
            numbers_used[n] += 1
            arr[depth] = n
            backtracking(depth + 1, n)
            numbers_used[n] -= 1
    arr[depth] = ""

backtracking(0, 1)