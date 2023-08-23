from sys import stdin

N, M = map(int, stdin.readline().split())

castle: list[list[bool]] = [[tile == "X" for tile in stdin.readline()] for _ in range(N)]
rows: list[bool] = [False for _ in range(N)]
cols: list[bool] = [False for _ in range(M)]

cnt: int = 0

# print("1. Check the castle")
for i in range(N):
    for j in range(M):
        if castle[i][j]:
            if not rows[i]:
                # print(f">>> row {i} has enough guards!")
                rows[i] = True
            if not cols[j]:
                # print(f">>> column {j} has enough guards!")
                cols[j] = True
# print("=> Result:")
# print("Rows:")
rowCnt: int = 0
for i, b in enumerate(rows):
    # print(f"[{i}] {b}")
    if not b:
        rowCnt += 1
# print("Cols:")
colCnt: int = 0
for i, b in enumerate(cols):
    # print(f"[{i}] {b}")
    if not b:
        colCnt += 1

print(max(rowCnt, colCnt))
