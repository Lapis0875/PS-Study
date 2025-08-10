input = open(0).readline
A, B = map(list, input().split())

for i in range(len(A)):
    if A[i] == '5':
        A[i] = '6'
for j in range(len(B)):
    if B[j] == '5':
        B[j] = '6'
max_res = min_res = int("".join(A)) + int("".join(B))
for i in range(len(A)):
    if A[i] == '6':
        A[i] = '5'
for j in range(len(B)):
    if B[j] == '6':
        B[j] = '5'
max_res = max(max_res, int("".join(A)) + int("".join(B)))
min_res = min(min_res, int("".join(A)) + int("".join(B)))
print(min_res, max_res)