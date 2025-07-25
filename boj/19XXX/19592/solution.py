input = open(0).readline

# 매개변수 탐색 (Parametric Search)
# 1. 주어진 조건(결정 문제)의 답이 NNNN...NYYY...Y 형태로 주어졌을 때, Y가 최초로 나오는 지점을 찾는 방식으로 최솟값을 찾는 최적화 문제를 풀 수 있다.
# 최솟값을 구하는 매개변수 탐색에서, 조건에 따라 범위는 아래와 같이 좁혀진다:
# decision(M) = False -> [M + 1, E]
# decision(M) = True -> [S, M]

for _ in range(int(input())):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    # 자신을 제외한 참가자들 중 가장 빨리 통과한 선수가 걸린 시간을 계산한다.
    fastest_record = X
    for i in range(N - 1):
        fastest_record = min(fastest_record, X / V[i])
    
    my_record = X / V[-1]  # 자신의 기록은 항상 마지막에 주어진다.
    if my_record < fastest_record:  # 굳이 부스터를 쓰지 않고도 이미 단독 우승이 가능한 경우
        print(0)
        continue

    l = 1       # 부스터를 최솟값 (부스터 사용량은 정수임)
    r = Y + 1   # 부스터의 최대 한계값 + 1. 부스터를 한계 이상으로 사용한 경우는 단독 우승이 불가능한 경우로 판단한다.
    while l < r:
        mid = (l + r) // 2
        # 부스터를 사용했을 때, 최소 시간 계산 (결정 문제)
        total_time = (X - mid) / V[-1] + 1 if mid > 0 else X / V[-1] # 최초 1초는 부스터 사용
        if total_time >= fastest_record: # 공동 우승까지는 원하지 않는 경우이므로, 같은 시간이 걸리는 경우는 N으로 처리
            l = mid + 1
        else:
            r = mid
    if l > Y:
        print(-1)
    else:
        print(r)