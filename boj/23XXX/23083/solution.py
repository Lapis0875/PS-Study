input = open(0).readline
MOD = 1_000_000_007
N, M = map(int, input().split())
K = int(input())
path = [[0] * M for _ in range(N)] # 장애물이 있는 칸은 -1, 나머지 칸은 해당 칸에 도달하기 위한 거리가 된다.
PREV_MOVE = (
    ((0, -1), (-1, -1), (-1, 0)), # 홀수 열로의 이동
    ((1, -1), (0, -1), (-1, 0)), # 짝수 열로의 이동
)

for _ in range(K):
    r, c = map(lambda i: int(i) - 1, input().split()) # 인덱스를 0부터 시작하도록 변환한다.
    path[r][c] = -1 # 장애물 위치를 -1로 표시한다.

path[0][0] = 1 # 처음 출발점은 항상 1이다.

# 배열 번호를 0부터 N-1까지로 사용하기 위해, 열의 홀수/짝수 여부가 반대로 계산된다.
# c % 2 == 0이라면 홀수 열, c % 2 == 1이라면 짝수 열이다.

# (1, 1)에서 (N, M)까지 채워나간다.
for c in range(M):
    for r in range(N):
        if path[r][c] == -1: # 장애물이 있는 칸은 건너뛴다.
            continue
    
    for dr, dc in PREV_MOVE[c % 2]:
        pr = r + dr
        pc = c + dc
        if 0 <= pr < N and 0 <= pc < M and path[pr][pc] != -1:
            path[r][c] = (path[r][c] + path[pr][pc]) % MOD

print(path[N - 1][M - 1])