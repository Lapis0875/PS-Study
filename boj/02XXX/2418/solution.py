input = open(0).readline
H, W, L = map(int, input().split())
DIFF = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
letters = [input().rstrip() for _ in range(H)]
word = input().rstrip()

cnt = 0
memo = [[[-1 for _ in range(L)] for _ in range(W)] for _ in range(H)]
def dfs(r, c, depth):
    if depth == L:
        return 1
    
    if memo[r][c][depth] != -1:
        return memo[r][c][depth]
    
    res = 0
    for dr, dc in DIFF:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < H and 0 <= nc < W and letters[nr][nc] == word[depth]:
            res += dfs(nr, nc, depth + 1)
    memo[r][c][depth] = res
    return res

for r in range(H):
    for c in range(W):
        if letters[r][c] == word[0]:
            cnt += dfs(r, c, 1)

print(cnt)