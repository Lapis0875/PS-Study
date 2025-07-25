input = open(0).readline
N, M = map(int, input().split())
A = set()
for num in map(int, input().split()):
    A.add(num)

arr = [0 for _ in range(M)]
result = set()

def backtracking(depth):
    if depth == M:
        result.add(tuple(arr))
        return

    for num in A:
        if num >= arr[depth - 1]:
            arr[depth] = num
            backtracking(depth + 1)
            arr[depth] = 0
    
backtracking(0)
result = sorted(result)
print("\n".join(" ".join(map(str, r)) for r in result))