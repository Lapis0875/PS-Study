input = open(0).readline
A = input().strip()
B = input().strip()
a_length = len(A)
b_length = len(B)

LCS = [[0] * (a_length + 1) for _ in range(b_length + 1)]
max_lcs = 0
for b_i in range(1, b_length + 1):
    for a_i in range(1, a_length + 1):
        if A[a_i - 1] == B[b_i - 1]:
            LCS[b_i][a_i] = LCS[b_i - 1][a_i - 1] + 1
            max_lcs = max(max_lcs, LCS[b_i][a_i])
        else:
            LCS[b_i][a_i] = 0

print(max_lcs)