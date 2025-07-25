from collections import Counter
input = open(0).readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
output = [0 for _ in range(M)]
result = set()
original_counter = Counter(A)
output_counter = {key: 0 for key in original_counter.keys()}

def dfs(depth):
    if depth == M:
        result.add(tuple(output))
        return
    
    for i in range(N):
        if output_counter[A[i]] < original_counter[A[i]]:
            output[depth] = A[i]
            output_counter[A[i]] += 1
            dfs(depth + 1)
            output[depth] = 0
            output_counter[A[i]] -= 1

dfs(0)

for r in sorted(result):
    print(" ".join(map(str, r)))
