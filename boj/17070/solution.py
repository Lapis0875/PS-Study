input = open(0).readline
N = int(input())
Room = tuple(tuple(map(int, input().split())) for _ in range(N))   # N x N 크기의 격자

# Constants
RIGHT = EMPTY = 0
DOWN = 1
DIAGONAL = 2

cache = {}
def dfs(r, c, direction):
    if r == N - 1 and c == N - 1:
        return 1
    if (r, c, direction) in cache:
        return cache[(r, c, direction)]
    
    count = 0   
    if direction == RIGHT:
        if c < N - 1 and Room[r][c+1] == EMPTY:
            if r < N - 1 and Room[r+1][c] == EMPTY and Room[r+1][c+1] == EMPTY:
                count += dfs(r + 1, c + 1, DIAGONAL)
            count += dfs(r, c + 1, RIGHT)
    elif direction == DOWN:
        if r < N - 1 and Room[r+1][c] == EMPTY:
            if c < N - 1 and Room[r][c+1] == EMPTY and Room[r+1][c+1] == EMPTY:
                count += dfs(r + 1, c + 1, DIAGONAL)
            count += dfs(r + 1, c, DOWN)
    else: # DIAGONAL
        if c < N - 1 and Room[r][c+1] == EMPTY:
            if r < N - 1 and Room[r+1][c] == EMPTY and Room[r+1][c+1] == EMPTY:
                count += dfs(r + 1, c + 1, DIAGONAL)
            count += dfs(r, c + 1, RIGHT)
        if r < N - 1 and Room[r+1][c] == EMPTY:
            count += dfs(r + 1, c , DOWN)

    cache[(r, c, direction)] = count
    return count

print(dfs(0, 1, RIGHT))
