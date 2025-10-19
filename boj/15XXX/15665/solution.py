input = open(0).readline
N, M = map(int, input().split())
numbers = {}
for n in sorted(map(int, input().split())):
    numbers[n] = numbers.get(n, False) or True

arr = [0] * M

def backtracking(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for n in numbers:
        arr[depth] = n
        backtracking(depth + 1)
    arr[depth] = ""

backtracking(0)