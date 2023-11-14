from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())
for _ in range(T):
    K: Final[int] = int(stdin.readline())
    d: Final[list[int]] = list(map(int, stdin.readline().split()))
    R: Final[list[int]] = [0] * (K + 1)
    for i in range(1, K + 1):
        R[i] = R[i - 1] + d[i - 1]

    DP: list[list[int]] = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(K):
        DP[i][i] = d[i]                             # 부분 파일의 길이가 1인 경우는 미리 DP 테이블에 저장해둔다.
    
    for file_length in range(2, K + 1):                 # 부분 파일의 길이. 1개짜리 파일은 굳이 합칠 필요 없으니 계산하지 않고 넘김.
        for i in range(K - file_length + 1):            # 합치기 시작할 파일의 인덱스
            j: int = i + file_length - 1                # 합칠 파일의 끝 인덱스
            DP[i][j] = min(DP[i][k] + DP[k+1][j] for k in range(i, j)) + sum(d[i:j+1])

    print(DP[0][K-1])
