from sys import stdin

A2B_CNT, B2A_CNT = map(int, stdin.readline().split())
A2B = sorted(map(int, stdin.readline().split()), reverse=True)
B2A = sorted(map(int, stdin.readline().split()), reverse=True)

A2B_IDX = 0
B2A_IDX = 0
a_cnt = 1
b_cnt = 0
while A2B_IDX < A2B_CNT and B2A_IDX < B2A_CNT:      # 양쪽 모두 여분의 멀티탭이 있는 동안
    if b_cnt == 0:                                  # 남은 B 단자가 없는 경우
        b_cnt += A2B[A2B_IDX]                       # 가장 많은 수의 B단자를 가진 A->B 멀티탭을 1개 사용
        A2B_IDX += 1
        a_cnt -= 1
    while B2A_IDX < B2A_CNT and b_cnt > 0:          # B단자가 남아있고, B->A 멀티탭이 남아있는 동안
        a_cnt += B2A[B2A_IDX]                       # 가장 많은 수의 A단자를 가진 B->A 멀티탭을 가능한만큼 사용
        B2A_IDX += 1                                # 남은 B단자에 전부 연결하거나, 남아있는 B->A 멀티탭을 전부 쓸 때까지 반복.
        b_cnt -= 1

print(a_cnt)