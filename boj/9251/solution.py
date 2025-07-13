input = open(0).readline
A = input().strip()
B = input().strip()
a_length = len(A)
b_length = len(B)

LCS = [[0 for _ in range(a_length + 1)] for _ in range(b_length + 1)]

for b_idx in range(1, b_length + 1):
    for a_idx in range(1, a_length + 1):
        if A[a_idx - 1] == B[b_idx - 1]:
            LCS[b_idx][a_idx] = LCS[b_idx - 1][a_idx - 1] + 1
        else:
            LCS[b_idx][a_idx] = max(LCS[b_idx - 1][a_idx], LCS[b_idx][a_idx - 1])

print(LCS[b_length][a_length])