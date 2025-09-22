input = open(0).readline
N = int(input())
A = list(map(int, input().split()))
OP_LIMIT = list(map(int, input().split()))
max_value = -1_000_000_001
min_value = 1_000_000_001

def div(l, r):
    negative = False
    if l < 0:
        negative = True
    if r < 0:
        negative = not negative
    l = abs(l) // abs(r)
    if negative:
        l *= -1
    return l

OPS = ((0, lambda l, r: l + r), (1, lambda l, r: l - r), (2, lambda l, r: l * r), (3, div))

def backtrack(depth, expr_result):
    if depth == N - 1:
        global max_value, min_value
        max_value = max(expr_result, max_value)
        min_value = min(expr_result, min_value)
        return
    
    for op_idx, op_func in OPS:
        if OP_LIMIT[op_idx] > 0:
            OP_LIMIT[op_idx] -= 1
            backtrack(depth + 1, op_func(expr_result, A[depth + 1]))
            OP_LIMIT[op_idx] += 1

backtrack(0, A[0])
print(f"{max_value}\n{min_value}")