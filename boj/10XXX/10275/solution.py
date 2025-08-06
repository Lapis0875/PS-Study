input = open(0).readline
for _ in range(int(input())):
    N, A, B = map(int, input().split())
    if A % 2 == 1: # 홀수 단위로 자르려면 무조건 1까지 나눠야 한다.
        print(N)
    else:
        a_n = 1
        b_n = 1
        a_cnt = 0
        b_cnt = 0
        while a_n & A == 0:
            a_cnt += 1
            a_n <<= 1
        while b_n & B == 0:
            b_cnt += 1
            b_n <<= 1
        print(N - min(a_cnt, b_cnt))
