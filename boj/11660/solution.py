input = open(0).readline

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
prefix_sum = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                prefix_sum[i][j] = arr[0][0]
            else:
                prefix_sum[i][j] = arr[i][j] + prefix_sum[i][j - 1]
        elif j == 0:
            prefix_sum[i][j] = arr[i][j] + prefix_sum[i - 1][j]
        else:
            prefix_sum[i][j] = arr[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().strip().split()) # 실제 인덱스는 0부터 시작하므로 1 줄인다.
    
    # 경우의 수 처리
    if x1 == 0:
        if y1 == 0: # 추가 계산이 필요 없는 경우.
            print(prefix_sum[x2][y2])
        else:  # y1이 0이 아닌 경우
            print(prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1])
    elif y1 == 0:  # x1이 0이 아닌 경우
        print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2])
    else:   # 일반적인 경우
        print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])