from heapq import heappush, heappop
input = open(0).readline
board = [[False] * 300 for _ in range(300)]
queue = []
KNIGHT_MOVES = (
    (-2, -1), (-1, -2), 
    (1, -2), (2, -1), 
    (-2, 1), (-1, 2),
    (1, 2), (2, 1)
)

def init_board(n):
    queue.clear()
    for r in range(n):
        for c in range(n):
            board[r][c] = False

def move_knight(n, start, end):
    init_board(n)
    heappush(queue, (0, *start))
    while queue:
        cnt, r, c = heappop(queue)

        for dr, dc in KNIGHT_MOVES:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                board[nr][nc] = True
                if nr == end[0] and nc == end[1]:
                    return cnt + 1
                heappush(queue, (cnt + 1, nr, nc))

for _ in range(int(input())):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start[0] == end[0] and start[1] == end[1]:
        print(0)
    else:
        res = move_knight(N, start, end)
        print(res)
