from sys import stdin

A2B_CNT, B2A_CNT = map(int, stdin.readline().split())
A2B = sorted(map(int, stdin.readline().split()), reverse=True)
B2A = sorted(map(int, stdin.readline().split()), reverse=True)

# 단계별로 A -> B -> A -> B... 를 반복, 반복하며 각 단계에 사용할 수 있는 멀티탭 중 단자 개수가 가장 많은것부터 차례로 고른다.
# 이때, A -> B에서는 이후 다시 B -> A로 돌아올 수 있도록 남아있는 멀티탭의 개수에 맞게 고려해야 한다.
# 예를 들어, 현재 남아있는 A 단자는 2개인데 B->A 멀티탭이 3개라면 다시 A 단자로 돌아올 수 있으므로 멀티탭을 연결해도 된다.
# 반대로, 남아있는 A단자는 5개인데 B->A멀티탭이 3개라면 굳이 A->B를 4개이상 연결할 필요 없다.
# 정리하면, A->B 로 연결할 때는 남아있는 B->A 멀티탭의 개수와 A단자의 개수를 비교해 연결하고
# B->A는 그냥 B단자를 최대한 많이 A단자로 바꿔주면 된다!

A2B_IDX = 0
def get_A2B(cnt):
    global A2B_IDX
    v = A2B[A2B_IDX:A2B_IDX + cnt]
    A2B_IDX += cnt
    return sum(v)

B2A_IDX = 0
def get_B2A(cnt):
    global B2A_IDX
    v = B2A[B2A_IDX:B2A_IDX + cnt]
    B2A_IDX += cnt
    return sum(v)

a_cnt = 1
b_cnt = 0
while A2B_IDX < A2B_CNT and B2A_IDX < B2A_CNT:
    # print(f"{'A->B' if flag else 'B->A'}: a_cnt = {a_cnt}, b_cnt = {b_cnt}, A2B_CNT = {A2B_CNT}, B2A_CNT = {B2A_CNT}")
    if b_cnt == 0:  # A -> B 연결
        if B2A_CNT >= a_cnt:
            # print(": B2A_CNT >= a_cnt => A 단자 전체에 A->B를 연결한다.\n")
            # A->B 멀티탭을 전부 A 단자에 연결한다.
            b_cnt += get_A2B(a_cnt)
            a_cnt = 0
        else:   # 남아있는 B->A 멀티탭의 개수가 현재 A 단자 개수보다 적다면,
            # A->B 멀티탭이 B->A보다 많다면 B->A 개수만큼, 그렇지 않다면 A->B 개수만큼 연결한다. 이후 B->A 멀티탭을 연결하고 종료.
            # print(": B2A_CNT < a_cnt => A 단자 중 B2A만큼만 A->B를 연결한다.\n")
            diff = B2A_CNT if A2B_CNT > B2A_CNT else A2B_CNT
            a_cnt -= diff
            b_cnt += get_A2B(diff)
    else:  # B -> A
        # B->A 멀티탭을 가능한대로 전부 B 단자에 연결한다.
        if b_cnt >= B2A_CNT: # B->A 멀티탭이 남은 B 단자 개수보다 적을 때
            # => 남은 B->A 멀티탭을 전부 연결하고 비운다.
            # print(": b_cnt >= B2A_CNT => B 단자 중 B2A만큼만 B->A를 연결한다.\n")
            b_cnt -= B2A_CNT
            a_cnt += get_B2A(B2A_CNT)
            break
        else:  # 남아있는 B->A 멀티탭의 개수가 현재 B 단자 개수보다 많을 때
            # => B 단자 전부 B->A 멀티탭에 연결한다.
            # print(": b_cnt < B2A_CNT => B 단자 전체에 B->A를 연결한다.\n")
            a_cnt += get_B2A(b_cnt)
            b_cnt = 0

print(a_cnt)