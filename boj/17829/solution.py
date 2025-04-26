from sys import stdin

N = int(stdin.readline().strip())                   # N은 2의 거듭제곱 꼴
matrix: list[list[int]] = []    # N x N 행렬
for i in range(N):
    matrix.append(list(map(int, stdin.readline().strip().split())))


def pulling(x: int, y: int) -> int:     # logN
    return sorted((matrix[x][y], matrix[x][y + 1], matrix[x + 1][y], matrix[x + 1][y + 1]))[2]


size: int = N
while size > 1:
    size //= 2
    for i in range(0, size):
        for j in range(0, size):
            matrix[i][j] = pulling(i * 2, j * 2)    # 2x2 행렬에서 2번째 큰 수를 구함. 이때 x, y는 2x2행렬의 좌상단 좌표.
    # NxN 행렬이 N/2 x N/2 행렬로 줄어듬. 기존 행렬 배열을 수정하므로, 동일 연산 유지 가능.

print(matrix[0][0])
