input = open(0).readline
for _ in range(int(input())):
    N, A, B = map(int, input().split())
    if A % 2 == 1: # 홀수 단위로 자르려면 무조건 1까지 나눠야 한다.
        print(N)
    else:
        magic_cnt = -1
        total_gold = 1 << N # 2^N
        while A > 0:
            if A >= total_gold:
                A -= total_gold
            total_gold >>= 1
            magic_cnt += 1
        print(magic_cnt)
    