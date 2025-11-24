input = open(0).readline

MOVE = ((1, 0), (0, 1), (-1, 0), (0, -1), (0, 0))
R, C, T = map(int, input().split())

room = [[""] * 100 for _ in range(100)]
start = None
for r in range(R):
    for c, tile in enumerate(input().rstrip()):
        if tile == "G":
            start = (r, c)
            tile = "."
        room[r][c] = tile

max_cnt = 0
def backtracking(time, cnt, r, c):
    if time == T:
        global max_cnt
        max_cnt = max(max_cnt, cnt)
        return

    for dr, dc in MOVE:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if room[nr][nc] == "S":
                room[nr][nc] = "."
                backtracking(time + 1, cnt + 1, nr, nc)
                room[nr][nc] = "S"
            elif room[nr][nc] == ".":
                backtracking(time + 1, cnt, nr, nc)

backtracking(0, 0, *start)
print(max_cnt)