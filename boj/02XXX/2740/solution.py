input = open(0).readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)]

# 행렬 곱셈 직접 하기
for i in range(N):
    for j in range(K): # 행렬 곱의 결과인 N x K 행렬의 각 원소는
        for k in range(M): #
            result[i][j] += A[i][k] * B[k][j] # A의 각 열과 B의 각 행을 곱한 값이다.

for row in result:
    print(*row)

# TODO: 추후 슈트라센 행렬 곱 알고리즘도 구현해두기
