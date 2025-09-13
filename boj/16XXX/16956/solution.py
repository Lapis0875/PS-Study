input = open(0).readline
R, C = map(int, input().split())
Map = [list(map(lambda s: "D" if s == "." else s, input().rstrip())) for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
diff = ((-1, 0), (1, 0), (0, 1), (0, -1))
wolf_can_meet = False

def dfs(r, c):
    for dr, dc in diff:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and Map[nr][nc] != "D":
            visited[nr][nc] = True
            if Map[nr][nc] == "S":
                return True
            
            if dfs(nr, nc):
                return True

for r in range(R):
    for c in range(C):
        if Map[r][c] == "W" and not visited[r][c]:
            wolf_can_meet = dfs(r, c)
        if wolf_can_meet:
            break
    if wolf_can_meet:
        break

if wolf_can_meet:
    print("0")
else:
    print("1")
    print("\n".join("".join(row) for row in Map))
