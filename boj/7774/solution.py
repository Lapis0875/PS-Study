from sys import stdin

A2B_CNT, B2A_CNT = map(int, stdin.readline().split())
A2B = sorted(map(int, stdin.readline().split()), reverse=True)
B2A = sorted(map(int, stdin.readline().split()), reverse=True)

A2B_IDX = 0
B2A_IDX = 0
a_cnt = 1
b_cnt = 0
while A2B_IDX < A2B_CNT and B2A_IDX < B2A_CNT:
    if b_cnt == 0:
        b_cnt += A2B[A2B_IDX]
        a_cnt -= 1
        A2B_IDX += 1
    
    diff = b_left if b_cnt > (b_left := B2A_CNT - B2A_IDX) else b_cnt
    a_cnt += sum(B2A[B2A_IDX:B2A_IDX + diff])
    B2A_IDX += diff
    b_cnt = 0

print(a_cnt)