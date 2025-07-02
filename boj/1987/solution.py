input = open(0).readline
R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]  # R x C 크기의 격자.

A_idx = ord('A')
visited = {chr(A_idx + i): False for i in range(26)}

result = 0  # 가장 긴 경로의 길이
def dfs(y, x, distance = 1):
    next_dfs = 0
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            if not visited[board[ny][nx]]:
                next_dfs += 1
                visited[board[ny][nx]] = True
                dfs(ny, nx, distance + 1)
                visited[board[ny][nx]] = False
    if next_dfs == 0:  # 더 이상 갈 곳이 없는 경우.
        global result
        result = max(result, distance)

visited[board[0][0]] = True  # 시작 위치 방문 처리
dfs(0, 0)
print(result)  # 가장 긴 경로의 길이 출력