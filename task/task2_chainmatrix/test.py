from typing import Final

N: int = 6
d: Final[list[int]] = [4, 3, 7, 1, 3, 3, 5]                             # d0 ~ dN
P: list[list[int]] = [[0 for _ in range(N + 1)] for _ in range(N + 1)]  # 1번 인덱스부터 사용하기 위해서, N + 1 크기로 설정.

def minmult(N: int, d: list[int], P: list[list[int]]) -> int:
    """
    교재의 minmult 의사코드를 구현한 함수.
    최소 곱셈 횟수를 가지는 행렬 곱셈 순서를 구하고, 이때의 총 곱셈 횟수를 반환한다.

    Args:
        N (int): 행렬의 개수
        d (list[int]): d0~dN의 각 행렬의 길이 정보
        P (list[list[int]]): 곱셈 순서를 저장할 행렬 (2차원 배열)

    Returns:
        int: 주어진 행렬들의 최소 곱셈 횟수
    """
    i: int; j: int; k: int; diagonal: int
    M: list[list[int]] = [[0] * (N + 1) for _ in range(N + 1)]          # 1번 인덱스부터 사용하기 위해서, N + 1 크기로 설정.
    for diagonal in range(1, N):
        for i in range(1, N - diagonal + 1):
            j = i + diagonal
            M[i][j], k = min((M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j], k) for k in range(i, j))
            P[i][j] = k
        print(f"diagonal = {diagonal}")
        print_array(N, M)
        print()
    return M[1][N]

def order(i: int, j: int):
    """
    교재의 order 의사코드를 구현한 함수.
    최소의 곱셈 순서를 출력한다.

    Args:
        i (int): 곱셈할 시작 행렬의 인덱스
        j (int): 곱셈할 끝 행렬의 인덱스
    """
    if i == j:
        print(f"A{i}", end="")
    else:
        k = P[i][j]
        print("(", end="")
        order(i, k)
        order(k + 1, j)
        print(")", end="")

def print_array(n: int, array: list[list[int]]):
    """행렬의 상태를 출력하기 위한 함수

    Args:
        n (int): 행렬의 크기
        array (list[list[Any]]): 출력할 행렬
    """
    # 인덱스를 1부터 사용하기 위해, 크기를 N + 1로 설정한 점을 반영한다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(format(array[i][j], "3d"), end=' ')    # INF와 글자 수를 맞추기 위해, 모든 숫자가 최소 3자리의 문자열로 출력되게 한다.
        print()
        
print(minmult(N, d, P))
order(1, N)
print()