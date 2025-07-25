from sys import stdin


S = stdin.readline().strip()
Q = int(stdin.readline().strip())
acc_count = [[0 for _ in range(26)] for _ in range(len(S))]     # [각 문자에 대한 누적 개수] 의 누적 합

for i, c in enumerate(S):
    for j in range(26):   # a ~ z 에 대한 누적 개수를 계산한다.
        if i == 0:
            acc_count[i][j] = 1 if ord(c) == ord("a") + j else 0
        else:
            acc_count[i][j] = acc_count[i - 1][j] + (1 if ord(c) - ord("a") == j else 0)

for i in range(Q):
    c, L, R = stdin.readline().strip().split()
    L = int(L)
    R = int(R)
    idx = ord(c) - ord("a")
    if L > 0:
        print(acc_count[R][idx] - (acc_count[L - 1][idx]))
    else:
        print(acc_count[R][idx])
