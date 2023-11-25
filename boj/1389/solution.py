from typing import Final
from sys import maxsize, stdin

# 코드에 사용할 상수들
INIT_PATH: Final[int] = 0       # 경로 배열의 초기값은 0으로 한다.
INF: Final[int] = maxsize       # 그래프의 인접 행렬에서, 연결되지 않은 두 정점 간의 가중치를 표현할 무한 값이다.

N: Final[int]                   # 정점의 개수
M: Final[int]                   # 간선의 개수
N, M = map(int, stdin.readline().split())

# 의사코드와 동일하게 하기 위해, 모든 배열은 인덱스를 1부터 사용한다. 따라서, 각 배열의 크기는 (N+1)*(N+1)이다.
# 0 번째 행과 열은 사용하지 않는다.
W: Final[list[list[int]]] = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    W[u][v] = 1
    W[v][u] = 1

# D와 P 행렬 생성
D: list[list[int]] = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

def floyd2(n: int, W: list[list[int]], D: list[list[int]]):
    """교재에 있는 floyd2 알고리즘을 구현한다.

    Args:
        n (int): 행렬의 크기
        W (list[list[int]]): 그래프의 인접 행렬
        D (list[list[int]]): 가중치 정보를 저장할 행렬
        P (list[list[int]]): 최단 경로 정보를 저장할 행렬
    """
    i: int
    j: int
    k: int
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = W[i][j]           # D 배열을 W 배열로 초기화
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                via: int = D[i][k] + D[k][j]
                if via < D[i][j]:
                    D[i][j] = via

def print_array(n: int, array: list[list[int]]):
    """행렬의 상태를 출력하기 위한 함수

    Args:
        n (int): 행렬의 크기
        array (list[list[Any]]): 출력할 행렬
    """
    # 인덱스를 1부터 사용하기 위해, 크기를 N + 1로 설정한 점을 반영한다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            weight: int = array[i][j]
            if weight == INF:                           # 무한 값은 INF로 출력한다.
                print("INF", end=' ')
            else:
                print(format(weight, "3d"), end=' ')    # INF와 글자 수를 맞추기 위해, 모든 숫자가 최소 3자리의 문자열로 출력되게 한다.
        print()

# 테스트 코드

floyd2(N, W, D)      # 1. floyd2 호출

min_person: int = 0
min_kb: int = INF
for i in range(1, N + 1):
    kebin_bacon: int = 0
    for j in range(1, N + 1):
        if j != i:
            kebin_bacon += D[i][j]
    if kebin_bacon < min_kb:
        min_person = i
        min_kb = kebin_bacon

print(min_person)   # 2. 케빈 베이컨 수가 제일 작은 사람 출력
