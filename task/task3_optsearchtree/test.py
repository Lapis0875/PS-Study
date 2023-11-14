from typing import Final
from print_tree import print_tree, tree             # print_tree.py에서 필요한 함수들을 가져온다.

key: list[str] = ["A", "B", "C", "D"]
N: Final[int] = 4
p: Final[list[float]] = [0, 0.25, 0.3, 0.15, 0.3]     # 인덱스를 1부터 사용하기 위해, 0번 원소를 추가한다.
    
# R[1..n+1][0..n] 이므로, n+2 * n+1 크기의 2차원 배열을 생성한다.
# 실제 행 크기는 n+1 이지만, 인덱스를 1부터 사용하기 위해 0번 행은 사용하지 않지만 코드상 편의를 위해 추가한다.
R: list[list[int]] = [[0 for _ in range(N + 1)] for _ in range(N + 2)]

def optsearchtree(n: int, p: list[float], R: list[list[int]]) -> float:
    """
    교쟈의 optsearchtree 알고리즘을 구현한다. 최적의 이진 검색 트리를 만든다.

    Args:
        n (int): 키의 개수
        p (list[float]): 각 키별 검색될 확률
        R (list[list[int]]): 두 인덱스 사이의 루트 노드 정보를 저장할 행렬

    Returns:
        float: 교재의 의사 코드에 있던 minavg 참조 변수이다. 파이썬에선 원시 타입의 참조를 매개변수에 넘길 수 없어, 함수의 반환 값으로 설정했다.
    """
    i: int
    j: int
    k: int
    diagonal: int
    
    # A[1..n+1][0..n] 이므로, n+2 * n+1 크기의 2차원 배열을 생성한다.
    # 실제 행 크기는 n+1 이지만, 인덱스를 1부터 사용하기 위해 0번 행은 사용하지 않지만 코드상 편의를 위해 추가한다.
    A: list[list[float]] = [[0 for _ in range(n + 1)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i-1] = 0
        A[i][i] = p[i]
        R[i][i-1] = 0
        R[i][i] = i
    
    A[n+1][n] = 0
    R[n+1][n] = 0
    
    for diagonal in range(1, n):                # 1 ~ n-1 반복
        for i in range(1, n - diagonal + 1):    # 1 ~ n-diagonal 반복
            j = i + diagonal
            A[i][j], k = min((A[i][k-1] + A[k+1][j] + sum(p[i:j+1]), k) for k in range(i, j+1))
            R[i][j] = k                         # i~j까지의 최적 이진 트리의 루트 노드의 인덱스.
        
        print(f"diagonal = {diagonal}")
        print("A:")
        print_probability(n, A)
        print("R:")
        print_index(n, R)
    
    return A[1][n]                              # minavg에 해당하는 값을 반환한다.

def print_index(n: int, array: list[list[int]]):
    """인덱스 행렬 (R)의 상태를 출력하기 위한 함수

    Args:
        n (int): 행렬의 크기
        array (list[list[int]]): 출력할 행렬
    """
    # 인덱스를 1부터 사용하기 위해, 크기를 N + 1로 설정한 점을 반영한다.
    for i in range(1, n + 2):
        for j in range(n + 1):
            print(array[i][j], end=' ')
        print()

def print_probability(n: int, array: list[list[float]]):
    """확률 행렬의 상태를 출력하기 위한 함수

    Args:
        n (int): 행렬의 크기
        array (list[list[float]]): 출력할 행렬
    """
    # 인덱스를 1부터 사용하기 위해, 크기를 N + 1로 설정한 점을 반영한다.
    for i in range(1, n + 2):
        for j in range(n + 1):
            # 실수 값을 일정한 간격으로 출력하기 위해, 소숫점 아래 3자리까지 출력되게 한다.
            print(format(array[i][j], ".3f"), end=' ')
        print()

print(optsearchtree(N, p, R))
root = tree(1, N, R, key)
if root is not None:
    print_tree(root, key)