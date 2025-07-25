from typing import Final
from sys import stdin, maxsize

# 코드에 사용할 상수들
INF: Final[int] = maxsize                   # 그래프의 인접 행렬에서, 연결되지 않은 두 정점 간의 가중치를 표현할 무한 값이다.

N: Final[int] = int(stdin.readline())       # 행렬의 크기

# 의사코드와 동일하게 하기 위해, 모든 배열은 인덱스를 1부터 사용한다. 따라서, 각 배열의 크기는 (N+1)*(N+1)이다.
# 0 번째 행과 열은 사용하지 않는다.
W: list[list[int]] = []
for _ in range(N):
    line: list[int] = []
    for cell in map(int, stdin.readline().split()):
        line.append(INF if cell == 0 else cell)
    W.append(line)

# D와 P 행렬 생성
D: list[list[int]] = [[0 for _ in range(N)] for _ in range(N)]

def floyd2(W: list[list[int]], D: list[list[int]]):
    """교재에 있는 floyd2 알고리즘을 구현한다.

    Args:
        W (list[list[int]]): 그래프의 인접 행렬
        D (list[list[int]]): 가중치 정보를 저장할 행렬
    """
    for i in range(N):
        for j in range(N):
            D[i][j] = W[i][j]           # D 배열을 W 배열로 초기화
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                via: int = D[i][k] + D[k][j]
                if via < D[i][j]:
                    D[i][j] = via

# 테스트 코드

floyd2(W, D)      # 1. floyd2 호출

for row in D:
    print(" ".join(map(lambda x: str(1 if x != INF else 0), row)))
