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

# 문제 답이랑 상관 없는, LCS의 가능한 값 찾기
lcs_length = LCS[b_length][a_length]
result = ["" for _ in range(lcs_length)]
cur_r = b_length
cur_c = a_length
for i in range(lcs_length):
    while True:
        if LCS[cur_r - 1][cur_c] == LCS[cur_r][cur_c]:
            cur_r -= 1
        elif LCS[cur_r][cur_c - 1] == LCS[cur_r][cur_c]:
            cur_c -= 1
        else:
            cur_r -= 1
            cur_c -= 1
            break
    result[i] = B[cur_r]
print(result[::-1])