from re import A
from typing import Final

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
    
    A: list[list[float]] = [[0] * (n + 1) for _ in range(n + 2)]  # A[1..n+1][0..n] 이므로, n+2 * n+1 크기의 2차원 배열을 생성한다.
    for i in range(1, n + 1):
        A[i][i-1] = 0
        A[i][i] = p[i]
        R[i][i-1] = 0
        R[i][i] = i
