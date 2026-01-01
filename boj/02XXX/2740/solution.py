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

# 슈트라센 행렬 곱 알고리즘
# 분할 정복을 이용한 행렬 곱셈 알고리즘으로, 행렬의 크기가 큰 경우에 일반적인 행렬 곱셈보다 빠르게 동작한다. O(n^2.81)
# 행렬의 크기가 2^N x 2^N 형태일 때에만 적용 가능하며 (아닌 경우 부족한 크기를 0으로 채워서 늘린다), 크기가 작은 행렬의 경우 O(n^3)인 일반 행렬 곱셈이 더 빠르다. (메모리의 cache-hit 비율이 더 높아 빠르다)

def strassen_matrix_multiply(A, B):
    
